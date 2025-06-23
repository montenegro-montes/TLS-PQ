#!/bin/bash

# =====================
# Function Definitions
# =====================

DOCKER_DIR="DockerTLS-PQ"
DOCKER_IMAGE=uma-pq-331 

INSTALL_DIR="./Applications"
PUMBA_BIN="$INSTALL_DIR/pumba"

show_menu() {
    echo "╔════════════════════════════════════════╗"
    echo "║      🐳  Docker & Protocol Menu        ║"
    echo "╠════════════════════════════════════════╣"
    echo "║ 1️⃣  Chek installation                   ║"
    echo "║ 2️⃣  Docker creation                     ║"
    echo "║ 3️⃣  Running Scenario                    ║"
    echo "║ 4️⃣  Exit                                ║"
    echo "╚════════════════════════════════════════╝"
}

###############################
#
# Docker Check
#
###############################

docker_installedAndRunning() {
# Check if Docker is installed
if ! command -v docker >/dev/null 2>&1; then
  echo "❌ Docker is not installed or not in PATH."
  echo "   Please install Docker: https://docs.docker.com/get-docker/"
  exit 1
fi

echo "🐳 Docker is installed. Proceeding with container execution..."

# Optional: Check Docker daemon is running
if ! docker info >/dev/null 2>&1; then
  echo "❌ Docker is installed but the daemon is not running."

  echo "✅ Running docker."
  docker desktop start

fi
}

###############################
#
# WhireShark
#
###############################


wireshark_installedAndRunning() {
  echo "🔍 Checking Wireshark installation..."

  if [[ "$(uname -s)" == "Darwin" ]]; then
    # macOS
    if [ -d "/Applications/Wireshark.app" ]; then
      echo "✅ Wireshark is installed on macOS."

    else
      echo "❌ Wireshark is not installed in /Applications."
      echo "   Download it from https://www.wireshark.org/download.html"
      exit 1
    fi

  else
    # Linux
    if command -v wireshark >/dev/null 2>&1; then
      echo "✅ Wireshark is installed."
    else
      echo "❌ Wireshark is not installed."
      echo "   Try: sudo apt install wireshark"
      exit 1
    fi
  fi

}

###############################
#
# Pumba Check
#
###############################

pumba_check() {


    # 1. Ensure ./Applications exists
    if [ ! -d "$INSTALL_DIR" ]; then
      echo "📁 Creating directory: $INSTALL_DIR"
      mkdir -p "$INSTALL_DIR"
    fi

    # 2. Check if pumba is already installed there
    if [ -f "$PUMBA_BIN" ]; then
      echo "✅ Pumba is at: $PUMBA_BIN"
      "$PUMBA_BIN" --version
 
    else   
        # 3. Detect OS and architecture
        OS=$(uname -s)
        ARCH=$(uname -m)

        case "$OS" in
          Linux)    os_tag="linux" ;;
          Darwin)   os_tag="darwin" ;;
          *) echo "❌ Unsupported OS: $OS"; exit 1 ;;
        esac

        case "$ARCH" in
          x86_64)   arch_tag="amd64" ;;
          arm64|aarch64) arch_tag="arm64" ;;
          *) echo "❌ Unsupported architecture: $ARCH"; exit 1 ;;
        esac

        # 4. Download the right binary
        VERSION="0.11.6"
        FILENAME="pumba_${os_tag}_${arch_tag}"
        URL="https://github.com/alexei-led/pumba/releases/download/${VERSION}/${FILENAME}"

        echo "⬇️ Downloading Pumba from:"
        echo "   $URL"
        curl -L -o "$PUMBA_BIN" "$URL"

        # 5. Make it executable
        chmod +x "$PUMBA_BIN"

        # 6. Done
        echo "✅ Pumba installed at $PUMBA_BIN"
        "$PUMBA_BIN" --version
    fi
      
}

###############################
#
# Docker Creation
#
###############################

docker_menu() {

    docker_installedAndRunning

    echo "----------------------------------------"
    echo "🐳 Docker Creation Options"
    echo "1) Build Docker (with cache)"
    echo "2) Build Docker (no cache)"
    echo "3) Verify installation"
    echo "4) Back to main menu"
    echo "----------------------------------------"
    read -p "👉 Choose an option [1-4]: " docker_choice
    echo ""

    # Verificar que el directorio y el Dockerfile existen
    if [[ ! -d "$DOCKER_DIR" ]]; then
        echo "❌ Error: Docker directory '$DOCKER_DIR' does not exist."
        return
    fi
    if [[ ! -f "$DOCKER_DIR/Dockerfile" ]]; then
        echo "❌ Error: No Dockerfile found in '$DOCKER_DIR'."
        return
    fi

    case $docker_choice in
        1)
            echo "🔧 Building Docker image with cache..."
            docker build -t "$DOCKER_IMAGE" "$DOCKER_DIR"
            ;;
        2)
            echo "♻️  Building Docker image without cache..."
            docker build --no-cache -t "$DOCKER_IMAGE" "$DOCKER_DIR"
            ;;
        3)  echo "🔍 Verifying OpenSSL PQ installation and TLS handshake performance..."
              # Set defaults if not already set
              SIG_ALG=${SIG_ALG:-ed25519}
              KEM_ALG=${KEM_ALG:-P-256}
              AUTH=${AUTH:-Single}
              NUM_RUNS=${NUM_RUNS:-1}
              TEST_TIME=${TEST_TIME:-1}


              echo "🔧 Using:"
              echo "   Signature Algorithm : $SIG_ALG"
              echo "   KEM Group           : $KEM_ALG"
              echo "   Auth Mode           : $AUTH"
              echo "   Runs                : $NUM_RUNS"
              echo

              docker run --rm --cap-add=NET_ADMIN \
                -e TEST_TIME=$TEST_TIME \
                -e KEM_ALG=$KEM_ALG \
                -e SIG_ALG=$SIG_ALG \
                -e NUM_RUNS=$NUM_RUNS \
                -e AUTH=$AUTH \
                -it $DOCKER_IMAGE perftestServer.sh > /tmp/test_output.log 2>&1

              echo "📈 Test Result (sample):"
              grep "connections in" /tmp/test_output.log | head -n 1 || echo "⚠️  No connections result found."

              if grep -q "connections in" /tmp/test_output.log; then
                echo
                echo "✅ Installation and test run completed successfully."
              else
                echo
                echo "❌ Installation verification failed. Check /tmp/test_output.log for details."
              fi
              echo
             ;;     
        4)
            return
            ;;
        *)
            echo "❌ Invalid option. Returning to main menu."
            ;;
    esac
}


###############################
#
# list_scenarios
#
###############################

list_scenarios() {
  SCENARIO_DIR="./Scenarios/"

  echo
  echo "📂 Available Scenarios:"
  echo "──────────────────────────────"

  if [ ! -d "$SCENARIO_DIR" ]; then
    echo "❌ Scenario directory not found: $SCENARIO_DIR"
    return 1
  fi

  local scenarios=()
  local count=0

  for dir in "$SCENARIO_DIR"/*/; do
    [ -d "$dir" ] || continue
    dirname=$(basename "$dir")
    scenarios+=("$dirname")
    echo " $((count + 1))) $dirname"
    count=$((count + 1))
  done

  if [ "$count" -eq 0 ]; then
    echo "⚠️  No scenario folders found in $SCENARIO_DIR"
    return 1
  fi

  echo
  while true; do
    read -p "👉 Enter the number of the scenario to run [1-$count]: " choice
    if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le "$count" ]; then
      selected_scenario="${scenarios[$((choice - 1))]}"
      echo "✅ You selected: $selected_scenario"
      SCENARIO_PATH="$SCENARIO_DIR/$selected_scenario"

      echo
      echo "⚠️  WARNING: All previous logs in this scenario may be overwritten."
      echo "   Please make a backup before continuing."
      read -p "❓ Are you sure you want to continue? (y/n): " confirm

      if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
        echo "❌ Operation cancelled."
        return 1
      fi

      # Ejecutar LauncherAll.sh
      if [ -x "$SCENARIO_PATH/LauncherAll.sh" ]; then
        echo "🚀 Executing LauncherAll.sh in $SCENARIO_PATH"
        (cd "$SCENARIO_PATH" && ./LauncherAll.sh)
        return 0
      else
        echo "❌ LauncherAll.sh not found or not executable in $SCENARIO_PATH"
        return 1
      fi
    else
      echo "❌ Invalid selection. Please enter a number between 1 and $count."
    fi
  done
}




###############################
#
# Check System
#
###############################

check_system() {
    echo " Verifying test ..."
    
    echo " 1. Docker Installed and running ..."
    docker_installedAndRunning
    echo " 2. Pumba Checking ..."
    pumba_check
    echo " 2. Wireshark Checking ..."
    wireshark_installedAndRunning
    echo
    read -p "🔁 Press Enter to return to the main menu..."

    return   
}


scenarios() {
    echo "🚀 Running TLS handshake test..."
    list_scenarios
}



analyze_results() {
    echo "📊 Analyzing results..."
    # ToDo
}

view_logs() {
    echo "📜 Viewing logs..."
    # ToDo
}

# =====================
# Main Menu Loop
# =====================

while true; do
    show_menu
    echo ""
    read -p "👉 Please enter your choice [1-4]: " choice
    echo ""
    case $choice in
        1) check_system ;;
        2) docker_menu  ;;
        3) scenarios ;;
        4) echo "👋 Goodbye!" ; exit 0 ;;
        *) echo "❌ Invalid option. Please try again." ;;
    esac
    echo ""
done
