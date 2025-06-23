#!/bin/bash

echo "🚀 Starting scenario batch execution..."

BASE_DIR="Time/loss"

# Recorremos todos los directorios delays_XXms
for dir in "$BASE_DIR"/loss_*; do
  [ -d "$dir" ] || continue

  LOSS_NAME=$(basename "$dir")            # e.g., delays_5ms
  LOSS_P=${LOSS_NAME#loss_}           # extrae 5ms

  echo "🔹 $LOSS_NAME - $LOSS_P"
  (
    cd "$dir/docker_scripts" || exit 1
    ./Launcher_Traditional.sh PERFORMANCE SINGLE 50 10 nocapture simple "$LOSS_P" 0 
  )
done

echo "✅ All scenarios executed."

# --- Process results ---
echo "🛠️  Processing Delays results..."
(
  cd Time || exit 1
  ./processAll.sh
)
echo "🏁 All processing complete."
