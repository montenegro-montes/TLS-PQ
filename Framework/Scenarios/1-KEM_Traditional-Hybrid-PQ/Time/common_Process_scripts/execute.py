import subprocess
import os
import argparse
import shutil  # Import shutil for file operations

# Configure argparse to receive the 'tag' parameter
parser = argparse.ArgumentParser(description="Process log files and generate plots.")
parser.add_argument('--tag', required=True, help='Suffix to append to generated image files, e.g., "_1ms".')
args = parser.parse_args()

# Define key directories
logs_dir = "logs"
scripts_dir = "process_scripts"
docker_scripts = "docker_scripts"
output_dir = "output"
tag = args.tag  # Get the tag from command-line arguments

# Create output and log directories if they do not exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# Subdirectories inside output
output_plot = os.path.join(output_dir, "plot")
output_csv = os.path.join(output_dir, "csv")

os.makedirs(output_csv, exist_ok=True)
os.makedirs(output_plot, exist_ok=True)

# Define input log files and corresponding output CSV files
logs = ["L1.log", "L3.log", "L5.log"]
csvs = [os.path.join(output_csv, log.replace(".log", ".csv")) for log in logs]
print("CSV files to be generated:")
processed_csvs = [csv.replace(".csv", ".processed.csv") for csv in csvs]

# Step 0: Move .log files to the logs directory if not already there
print("Moving .log files to the 'logs' folder...")
for log in logs:
    source_path = os.path.join(docker_scripts, log)
    destination_path = os.path.join(logs_dir, log)
    
    if os.path.exists(source_path) and not os.path.exists(destination_path):
        print(f"Moving {source_path} -> {destination_path}...")
        shutil.move(source_path, destination_path)
    elif not os.path.exists(source_path):
        print(f"File {source_path} does not exist.")
    else:
        print(f"{log} is already in {logs_dir}, no need to move.")

# Step 1: Run csv_process.py for each log file
print("Starting log processing...")
for log, csv_output in zip(logs, csvs):
    log_path = os.path.join(logs_dir, log)
    print(f"Processing {log_path} -> {csv_output}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "csv_process.py"),
        log_path,
        output_csv
    ], check=True)

    # Handle case where a directory is created instead of a CSV file
    if os.path.isdir(csv_output):
        generated_file = os.path.join(csv_output, os.path.basename(csv_output))
        if os.path.exists(generated_file):
            shutil.move(generated_file, csv_output)
            shutil.rmtree(csv_output)
        else:
            raise FileNotFoundError(f"Generated file not found inside {csv_output}.")

# Step 2: Run transformCSV.py on each generated CSV
print("\nTransforming CSV files...")
for csv in csvs:
    print(f"Transforming {csv}...")
    subprocess.run(["python3", os.path.join(scripts_dir, "transformCSV.py"), csv], check=True)

# Step 3: Generate plots with plotBox.py for each processed CSV
print("\nGenerating plots...")
for processed_csv in processed_csvs:
    print(f"Generating plot for {processed_csv}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "plotBox.py"),
        processed_csv,
        "--output_dir", output_plot,
        "--tag", tag
    ], check=True)

print("\n✅ All processing completed successfully!")
