#!/bin/bash

echo "🚀 Starting scenario batch execution..."


# --- Scenario 1 ---
echo "🔹 Size/HQC/HQC_Server"
(
  cd Size/HQC/HQC_Server/docker_scripts || exit 1
  ./Launcher_HQC.sh HANDSHAKE SINGLE
)

# --- Scenario 2 ---
echo "🔹 Time/Connections/Connections_Server"
(
  cd Time/Connections/Connections_Server/docker_scripts || exit 1
  ./Launcher_HQC.sh PERFORMANCE SINGLE
)

echo "✅ All scenarios executed."


# --- Process Size results ---
echo "🛠️  Processing Size results..."
(
  cd Size || exit 1
  ./processAll.sh
)

# --- Process Time results ---
echo "🛠️  Processing Time results..."
(
  cd Time || exit 1
  ./processAll.sh
)

echo "🏁 All processing complete."