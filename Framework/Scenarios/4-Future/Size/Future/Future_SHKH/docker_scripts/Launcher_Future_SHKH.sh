#!/bin/bash

#!/usr/bin/env bash
set -euo pipefail

###############################################################################
#  COMMAND LINE PARAMETERS
#
#  Usage: ./Launcher.sh [HANDSHAKE|PERFORMANCE] [MUTUAL|SINGLE] [NUM_RUNS] [TEST_TIME] [capture|captureKey|nocapture] [none|simple|stable|unstable] [loss-percent] [delay-ms]
###############################################################################

TYPE=${1:-PERFORMANCE}
AUTH_MODE=${2:-SINGLE}
NUM_RUNS=${3:-50}
TEST_TIME=${4:-10}
CAPTURE_MODE=${5:-nocapture}
NETWORK_PROFILE=${6:-none}
LOSS_PERC=${7:-0}
DELAY_MS=${8:-0}


USAGE="Usage: $0  [HANDSHAKE|PERFORMANCE] [MUTUAL|SINGLE] [NUM_RUNS] [TEST_TIME] [capture|captureKey|nocapture] [none|simple|stable|unstable] [loss-percent] [delay-ms]"

MUTUAL_AUTHENTICATION=false
os=""
###############################################################################
#  Input Validation
###############################################################################

# 1) Protocol
if [[ "$TYPE" != "PERFORMANCE" && "$TYPE" != "HANDSHAKE" ]]; then
    echo "$USAGE"
    exit 1
fi

# 2) Mutual authentication mode
if [[ "$AUTH_MODE" != "MUTUAL" && "$AUTH_MODE" != "SINGLE" ]]; then
    echo "Invalid authentication mode: must be 'MUTUAL' or 'SINGLE'."
    echo "$USAGE"
    exit 1
fi

# 3) Packet capture mode
if [[ "$CAPTURE_MODE" != "capture" && "$CAPTURE_MODE" != "captureKey" && "$CAPTURE_MODE" != "nocapture" ]]; then
    echo "Invalid capture mode: must be 'capture', 'captureKey', or 'nocapture'."
    echo "$USAGE"
    exit 1
fi

# 4) Network profile
if [[ "$NETWORK_PROFILE" != "none" && "$NETWORK_PROFILE" != "simple" && "$NETWORK_PROFILE" != "stable" && "$NETWORK_PROFILE" != "unstable" ]]; then
    echo "Invalid network profile: must be 'none', 'simple', 'stable', or 'unstable'."
    echo "$USAGE"
    exit 1
fi

# 5) Packet loss percentage (0–100)
if ! [[ "$LOSS_PERC" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
    echo "Invalid loss-percent: must be a number between 0 and 100 (e.g., 0.5, 25, 99.9)."
    echo "$USAGE"
    exit 1
fi

if (( $(echo "$LOSS_PERC < 0 || $LOSS_PERC > 100" | bc -l) )); then
    echo "Invalid loss-percent: must be between 0 and 100."
    echo "$USAGE"
    exit 1
fi

# 6) Delay in milliseconds (>= 0)
if ! [[ "$DELAY_MS" =~ ^[0-9]+$ ]] || (( DELAY_MS < 0 )); then
    echo "Invalid delay-ms: must be a non-negative integer."
    echo "$USAGE"
    exit 1
fi



###############################################################################
#  CONFIGURATION
###############################################################################


if [[ "$AUTH_MODE" == "mutual" ]]; then
   MUTUAL_AUTHENTICATION=true  
fi

 OQS_CONTAINER="uma-pq-331"
 OQS_SERVER_CIENT="TLSPQ"
 SIG_L1=("p256_falcon512" "p256_sphincssha2128fsimple" "p256_sphincssha2128ssimple" "p256_mayo1")
 SIG_L3=("p384_mldsa65" "p384_sphincssha2192fsimple" "p384_sphincssha2192ssimple" "p384_mayo3")
 SIG_L5=("p521_mldsa87" "p521_falcon1024" "p521_sphincssha2256fsimple" "p521_sphincssha2256ssimple" "p521_mayo5")
 KEMS_L1=("p256_mlkem512" "x25519_mlkem512" "mlkem512" )
 KEMS_L3=("p384_mlkem768" "x448_mlkem768" "mlkem768")
 KEMS_L5=("p521_mlkem1024" "mlkem1024")
 

#!/bin/bash



echo "*************************************"
echo "Parameters valid. Starting with:"
echo "  Type:            $TYPE"
echo "  Auth Mode:       $AUTH_MODE"
echo "  Capture Mode:    $CAPTURE_MODE"
echo "  Network Profile: $NETWORK_PROFILE"
echo "  Loss %:          $LOSS_PERC"
echo "  Delay (ms):      $DELAY_MS"
echo "  Executions:      $NUM_RUNS"
echo "  Time:            $TEST_TIME"

echo "  Signature L1:    ${SIG_L1[*]}   "
echo "  KEMS Level 1:    ${KEMS_L1[*]}"
echo "  Signature L3:    ${SIG_L3[*]}   "
echo "  KEMS Level 3:    ${KEMS_L3[*]}"
echo "  Signature L5:    ${SIG_L5[*]}   "
echo "  KEMS Level 5:    ${KEMS_L5[*]}"
echo "*************************************"

###############################################################################
#  Function: detect_platform
#    
###############################################################################

detect_platform() {
    os="$(uname -s)"
    case "$os" in
        Linux)
            echo "Runnig on Linux" ;;
        Darwin)
            echo "Runnig on macOS" ;;
        *)
            echo "Runnig on: $os" ;;
    esac
}

###############################################################################
#  Function: launch_edgeshark
#    
###############################################################################
launch_edgeshark() {
    # 1) Variables
    URL="https://github.com/siemens/edgeshark/raw/main/deployments/wget/docker-compose-localhost.yaml"
    COMPOSE_FILE="./docker-compose-localhost.yaml"  # ruta fija

    # 2) Descargar (si ha cambiado) el fichero de Compose
    mkdir -p "$(dirname "$COMPOSE_FILE")"
    wget -q --no-cache -O "$COMPOSE_FILE" "$URL"

    # 3) Comprobar si hay contenedores levantados
    #    --quiet -q return  IDs; if it is empty, there is no runnig container
    if [ -z "$(docker compose -f "$COMPOSE_FILE" ps -q)" ]; then
        echo "$(date '+%F %T') → No active containers. Running stack..." 
        docker compose -f "$COMPOSE_FILE" up -d 
    else
        echo "$(date '+%F %T') → It is runnig. Nothing to do." 
    fi
}
###############################################################################
#  Function: lauch_Wireshark
#    
###############################################################################

lauch_Wireshark_mac(){

     if [ -d "/Applications/Wireshark.app" ]; then
                    echo "Wireshark is installed, perfect!!!"

                    if ps aux | grep -i wireshark | grep -v grep > /dev/null; then         
                        echo "Wireshark is running."
                        # Espera a que el usuario esté listo
                        read -n 1 -s -r -p "Please save Wireshark data to run another experiment..."
                        echo ""
                        echo "Running now ... "
                        open -a Wireshark

                    else
                        echo "Wireshark is NOT running. Running now ... "
                        open -a Wireshark
                    fi 
            else
                echo "Wireshark is not installed in /Applications."
                exit 1
            fi

            # Espera a que el usuario esté listo
            read -n 1 -s -r -p "Configure Wireshark and press any key when you are ready to continue..."
            echo ""
}

###############################################################################
#  Function: lauch_Wireshark
#    
###############################################################################

launch_wireshark_linux() {
    # Check if the 'wireshark' command is available
    if command -v wireshark >/dev/null 2>&1; then
        echo "Wireshark is installed, perfect!!!"

        # Check if Wireshark is already running (as the current user)
        if pgrep -u "$USER" -x wireshark >/dev/null 2>&1; then
            echo "Wireshark is already running."
        else
            echo "Wireshark is NOT running. Starting now..."
            # Launch Wireshark in the background
            wireshark 
            # Give it a moment to start
            sleep 1
        fi

        # Wait for the user to save or inspect captures before proceeding
        read -n 1 -s -r -p "Please save Wireshark data to run another experiment, then press any key to continue..."
        echo ""
        read -n 1 -s -r -p "Configure Wireshark and press any key when you are ready to continue..."
        echo ""

    else
        echo "Wireshark is not installed. Please install it (e.g. Ubuntu/Debian: sudo apt install wireshark) and try again."
        exit 1
    fi
}
###############################################################################
#  Function: cleaning
#    
###############################################################################

cleaning(){
    docker kill $OQS_SERVER_CIENT &>/dev/null || true

    sleep 1
    docker container prune -f
    sleep 1
}

detect_platform

cleaning

if [[ "$CAPTURE_MODE" == "capture" || "$CAPTURE_MODE" == "captureKey" ]]; then
    echo ""
    echo "Launching edgeshark"
    launch_edgeshark
 fi   


for LEVEL in L1 L3 L5; do

    # Use indirect variable reference
    SIG_VAR="SIG_$LEVEL"
    KEM_VAR="KEMS_$LEVEL"

    eval "SIGS=(\"\${${SIG_VAR}[@]}\")"
    #SIG_ALG=${!SIG_VAR}
    eval "KEMS=(\"\${${KEM_VAR}[@]}\")"

    LOG_FILE="${LEVEL}.log"

    for  SIG_ALG in "${SIGS[@]}"; do
            echo "📄 Starting tests for $LEVEL (SIG: $SIG_ALG)"

            for KEM_ALG in "${KEMS[@]}"; do
               
                # Clean up any previous container
                docker rm -f "$OQS_SERVER_CIENT" 2>/dev/null || true


               if [[ "$TYPE" == "HANDSHAKE" ]]; then

                    echo "handshake"
                    echo "GET /" | docker run --rm --cap-add=NET_ADMIN \
                      --name "$OQS_SERVER_CIENT" \
                      -e TEST_TIME="$TEST_TIME" \
                      -e KEM_ALG="$KEM_ALG" \
                      -e SIG_ALG="$SIG_ALG" \
                      -e NUM_RUNS="$NUM_RUNS" \
                      -e AUTH="$AUTH_MODE" \
                      -e TYPE="$TYPE" \
                      -e TC_DELAY="${DELAY_MS}ms" \
                      -e TC_LOSS="${LOSS_PERC}%" \
                      -i "$OQS_CONTAINER" perftestServer.sh 2>&1 | tee -a "$LOG_FILE"
                else
                    docker run --rm --cap-add=NET_ADMIN \
                      --name "$OQS_SERVER_CIENT" \
                      -e TEST_TIME="$TEST_TIME" \
                      -e KEM_ALG="$KEM_ALG" \
                      -e SIG_ALG="$SIG_ALG" \
                      -e NUM_RUNS="$NUM_RUNS" \
                      -e AUTH="$AUTH_MODE" \
                      -e TYPE="$TYPE" \
                      -e TC_DELAY="${DELAY_MS}ms" \
                      -e TC_LOSS="${LOSS_PERC}%" \
                      -it "$OQS_CONTAINER" perftestServer.sh 2>&1 | tee -a "$LOG_FILE"
                fi

            done
    done        
done

sleep 3

cleaning
echo "✅  Cleanup complete. Tests finished."


