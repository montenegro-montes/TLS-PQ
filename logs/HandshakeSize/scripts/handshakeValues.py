import re
import sys
import os
import csv

def process_file(input_file_path):
    # Define the regex patterns for the command and handshake lines
    pattern_command = re.compile(r"Running /opt/oqssa/bin/perftestHandshakeServer.sh with SIG_ALG=(\w+) and KEM_ALG=(\w+-?\d*)")
    pattern_handshake = re.compile(r"SSL handshake has read (\d+) bytes and written (\d+) bytes")

    # Open the input file and read all lines
    try:
        with open(input_file_path, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    # Variables to store results
    results = []

    # Find all occurrences of the command pattern
    for line in content:
        # Search for command pattern
        match_command = pattern_command.search(line)
        if match_command:
            sig_alg = match_command.group(1)
            kem_alg = match_command.group(2)
            continue  # Skip to next line after finding the command pattern
        
        # Search for handshake pattern
        match_handshake = pattern_handshake.search(line)
        if match_handshake:
            read_bytes = match_handshake.group(1)
            written_bytes = match_handshake.group(2)
            results.append({
                'SIG_ALG': sig_alg,
                'KEM_ALG': kem_alg,
                'Read Bytes': read_bytes,
                'Written Bytes': written_bytes
            })

    if not results:
        print("No matching handshake lines found in the input file.")
        return

    # Write results to CSV file
    output_csv = f"{os.path.splitext(input_file_path)[0]}_handshake.csv"
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['SIG_ALG', 'KEM_ALG', 'Read Bytes', 'Written Bytes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print(f"CSV file '{output_csv}' has been generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)
