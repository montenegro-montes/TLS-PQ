import re
import sys
import os

def process_file(input_file_path):
    # Define the regex patterns for the command and certificate
    pattern_command = re.compile(r"Running /opt/oqssa/bin/perftestHandshakeServer.sh with SIG_ALG=(\w+) and KEM_ALG=(\w+-?\d*)")
    pattern_certificate = re.compile(r"-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----", re.DOTALL)

    # Open the input file and read all lines
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    # Find all occurrences of the command pattern
    matches = pattern_command.finditer(content)

    if not matches:
        print("No matching commands found in the input file.")
        return

    # Iterate over each match and process the corresponding certificate
    for match in matches:
        sig_alg = match.group(1)
        kem_alg = match.group(2)

        output_filename = f"{sig_alg}-{kem_alg}.crt"

        # Search for the corresponding certificate content after each command
        start_idx = match.end()  # Start searching from the end of the command match
        match_certificate = pattern_certificate.search(content, start_idx)
        if match_certificate:
            certificate_content = match_certificate.group(0)

            # Write the certificate content to the output file
            with open(output_filename, 'w') as outfile:
                outfile.write(certificate_content)

            print(f"Certificate saved to {output_filename}")
        else:
            print(f"Certificate not found for {sig_alg}-{kem_alg} in the input file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)

