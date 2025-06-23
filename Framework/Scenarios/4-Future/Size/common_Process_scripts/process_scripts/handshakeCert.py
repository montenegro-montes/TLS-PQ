import re
import sys
import os

def process_certificate(content, pattern_command, pattern_certificate, sig_alg_prefix='', output_dir='crt'):
    # Ensure the output directory exists, create it if necessary
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    matches = pattern_command.finditer(content)
    for match in matches:
        sig_alg = f"{sig_alg_prefix}{match.group(1)}"  # Add prefix for RSA if needed
        kem_alg = match.group(2)
        output_filename = os.path.join(output_dir, f"{sig_alg}-{kem_alg}.crt")

        # Search for the corresponding certificate content after each command
        start_idx = match.end()  # Start searching from the end of the command match
        match_certificate = pattern_certificate.search(content, start_idx)
        if match_certificate:
            certificate_content = match_certificate.group(0)

            # Write the certificate content to the output file
            with open(output_filename, 'w') as outfile:
                outfile.write(certificate_content)

            file_size = os.path.getsize(output_filename)

            print(f"Certificate saved to {output_filename} - File size: {file_size} bytes")
        else:
            print(f"Certificate not found for {sig_alg}-{kem_alg} in the input file.")

def process_file(input_file_path):
    # Define the regex patterns for the command and certificate
    pattern_command_sig_kem = re.compile(r"Running /opt/oqssa/bin/perftestHandshakeServer.sh with SIG_ALG=(\w+) and KEM_ALG=(\w+-?\d*)")
    pattern_command_rsa = re.compile(r"Running /opt/oqssa/bin/perftestHandshakeServerRSA.sh with SIG_KEY=rsa_keygen_bits:(\d+) and KEM_ALG=(\w+-?\d*)")
    pattern_command_ecdsa = re.compile(r"Running /opt/oqssa/bin/perftestHandshakeServerECDSA.sh with SIG_ALG=(\w+) and KEM_ALG=(\w+-?\d*)")
    pattern_certificate = re.compile(r"-----BEGIN CERTIFICATE-----(.*?)-----END CERTIFICATE-----", re.DOTALL)

    # Open the input file and read all lines
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    # If no matches found, return early
    if not (pattern_command_sig_kem.search(content) or pattern_command_rsa.search(content) or pattern_command_ecdsa.search(content)):
        print("No matching commands found in the input file.")
        return

    # Process each pattern with the corresponding prefix for RSA
    process_certificate(content, pattern_command_sig_kem, pattern_certificate)
    process_certificate(content, pattern_command_rsa, pattern_certificate, sig_alg_prefix="RSA-")
    process_certificate(content, pattern_command_ecdsa, pattern_certificate)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)
