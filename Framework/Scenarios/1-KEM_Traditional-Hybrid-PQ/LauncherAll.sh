#!/bin/bash

echo "🚀 Starting scenario batch execution..."

# --- Scenario 1 ---
echo "🔹 Size/Bytes/Bytes_Mutual"
(
  cd Size/Bytes/Bytes_Mutual/docker_scripts || exit 1
  ./Launcher_Traditional.sh HANDSHAKE MUTUAL
)

# --- Scenario 2 ---
echo "🔹 Size/Bytes/Bytes_Server"
(
  cd Size/Bytes/Bytes_Server/docker_scripts || exit 1
  ./Launcher_Traditional.sh HANDSHAKE SINGLE
)

# --- Scenario 3 ---
echo "🔹 Time/Connections/Connections_Mutual"
(
  cd Time/Connections/Connections_Mutual/docker_scripts || exit 1
  ./Launcher_Traditional.sh PERFORMANCE MUTUAL
)

# --- Scenario 4 ---
echo "🔹 Time/Connections/Connections_Server"
(
  cd Time/Connections/Connections_Server/docker_scripts || exit 1
  ./Launcher_Traditional.sh PERFORMANCE SINGLE
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