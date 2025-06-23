#!/bin/bash

echo "🚀 Starting scenario batch execution..."

BASE_DIR="Time/delays"

# Recorremos todos los directorios delays_XXms
for dir in "$BASE_DIR"/delays_*; do
  [ -d "$dir" ] || continue

  DELAY_NAME=$(basename "$dir")            # e.g., delays_5ms
  DELAY_MS=${DELAY_NAME#delays_}           # extrae 5ms
  DELAY_VALUE=${DELAY_MS%ms}               # elimina el sufijo 'ms' => 5

  echo "🔹 $DELAY_NAME"
  (
    cd "$dir/docker_scripts" || exit 1
    ./Launcher_Traditional.sh PERFORMANCE SINGLE 50 10 nocapture simple 0 "$DELAY_VALUE"
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
