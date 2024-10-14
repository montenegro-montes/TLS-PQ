import re
import sys
import os

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

    # Find all occurrences of the command patterns
    matches_sig_kem = pattern_command_sig_kem.finditer(content)
    matches_rsa = pattern_command_rsa.finditer(content)
    matches_ecdsa = pattern_command_ecdsa.finditer(content)

    if not matches_sig_kem and not matches_rsa and not matches_ecdsa:
        print("No matching commands found in the input file.")
        return

    # Process SIG_ALG and KEM_ALG patterns
    for match in matches_sig_kem:
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

    # Process RSA pattern
    for match in matches_rsa:
        sig_alg = f"RSA-{match.group(1)}"
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

    # Process ECDSA pattern
    for match in matches_ecdsa:
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
