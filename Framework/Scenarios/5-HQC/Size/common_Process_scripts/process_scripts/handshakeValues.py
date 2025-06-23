import re
import sys
import os
import csv

def process_file(input_file_path):
   # Define generic patterns
    patterns = {
        'sig_kem': re.compile(
            r"Running /opt/oqssa/bin/perftest(?:Handshake)?(?:Mutual|Server)?(?:ECDSA)?\.sh with SIG_ALG=(\w+) and KEM_ALG=(\w+(?:-\w+)?(?:\d+)?)"
        ),
        'rsa': re.compile(
            r"Running /opt/oqssa/bin/perftestHandshake(?:Mutual|Server)?RSA\.sh with SIG_KEY=rsa_keygen_bits:(\d+) and KEM_ALG=(\w+(?:-\w+)?(?:\d+)?)"
        ),
        'handshake': re.compile(
            r"SSL handshake has read (\d+) bytes and written (\d+) bytes"
        )
    }

    # Read input file
    try:
        with open(input_file_path, 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"❌ Error: File '{input_file_path}' not found.")
        exit(1)

    # Initialize state
    results = []
    current_sig_alg = None
    current_kem_alg = None

    # Parse each line
    for line in content:
        line = line.strip()

        # Match general SIG/KEM pattern
        m = patterns['sig_kem'].search(line)
        if m:
            current_sig_alg = m.group(1)
            current_kem_alg = m.group(2)
            continue

        # Match RSA-specific pattern
        m = patterns['rsa'].search(line)
        if m:
            current_sig_alg = f"RSA-{m.group(1)}"
            current_kem_alg = m.group(2)
            continue

        # Match handshake data
        m = patterns['handshake'].search(line)
        if m and current_sig_alg and current_kem_alg:
            results.append({
                'SIG_ALG': current_sig_alg,
                'KEM_ALG': current_kem_alg,
                'Read Bytes': int(m.group(1)),
                'Written Bytes': int(m.group(2)),
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
        print("Usage: python handshakeValues.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)
