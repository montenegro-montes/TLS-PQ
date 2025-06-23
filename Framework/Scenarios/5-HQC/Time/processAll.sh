#!/bin/bash

# Function to process a set of directories
process_directories() {
  base_path="$1"
  prefix="$2"

  for dir in "$base_path"/"${prefix}"*/; do
    tag="${dir##*/$prefix}"
    tag="${tag%/}"

    echo "📂 Processing $dir with tag $tag"

    # Copy the script and subfolder
    cp common_Process_scripts/execute.py "$dir" || { echo "❌ Failed to copy execute.py"; continue; }
    cp -r common_Process_scripts/process_scripts "$dir" || { echo "❌ Failed to copy process_scripts"; continue; }

    # Execute the script
    (
      cd "$dir" && python3 execute.py --tag "connections_$tag"
    )

    # Cleanup copied files
    rm -f "$dir/execute.py"
    rm -rf "$dir/process_scripts"
  done
}

# Process delays and loss directories
process_directories "Connections" "Connections_"
