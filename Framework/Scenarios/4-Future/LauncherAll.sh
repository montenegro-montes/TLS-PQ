#!/bin/bash

echo "🚀 Starting scenario batch execution..."

# --- Scenario 1 ---
echo "🔹 Size/Future/Future_SHKH"
(
  cd Size/Future/Future_SHKH/docker_scripts || exit 1
  ./Launcher_Future_SHKH.sh HANDSHAKE 
)

# --- Scenario 2 ---
echo "🔹 Size/Future/Future_SPKH"
(
  cd Size/Future/Future_SPKH/docker_scripts || exit 1
  ./Launcher_Future_SPKH.sh HANDSHAKE 
)

# --- Scenario 3 ---
echo "🔹 Time/Future/Future_SHKH"
(
  cd Time/Future/Future_SHKH/docker_scripts || exit 1
  ./Launcher_Future_SHKH.sh  PERFORMANCE 
)

# --- Scenario 4 ---
echo "🔹 Time/Future/Future_SPKH"
(
  cd Time/Future/Future_SPKH/docker_scripts || exit 1
  ./Launcher_Future_SPKH.sh  PERFORMANCE 
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