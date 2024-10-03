import re
import csv
import sys
import os

def process_file(input_file_path, output_file_path):
    # Define the regex patterns
    pattern_command = re.compile(r"^Running /opt/oqssa/bin/perftestServer.sh with SIG_ALG=(\w+) and KEM_ALG=([\w-]+)")
    pattern_command_rsa = re.compile(r"^Running /opt/oqssa/bin/perftestServerRSA.sh with SIG_ALG=rsa_keygen_bits:(\d+) and KEM_ALG=([\w-]+)")
    pattern_command_ecdsa = re.compile(r"^Running /opt/oqssa/bin/perftestServerECDSA.sh with SIG_ALG=(\w+) and KEM_ALG=([\w-]+)")
    pattern_connections = re.compile(r"(\d+) connections in ([\d\.]+)s; ([\d\.]+) connections/user sec")

    # Open the input file and read the lines
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists to store the filtered data
    commands = []
    connections = []
    connections_group = []

    # Process each line
    for line in lines:
        # Check for command pattern
        match_command = pattern_command.match(line)
        if match_command:
            sig_alg = match_command.group(1)
            kem_alg = match_command.group(2)
            commands.append((sig_alg, kem_alg))
            continue
        
        # Check for RSA command pattern
        match_command_rsa = pattern_command_rsa.match(line)
        if match_command_rsa:
            sig_alg = f"rsassa-pss-256"
            kem_alg = match_command_rsa.group(2)
            commands.append((sig_alg, kem_alg))
            continue

        # Check for ECDSA command pattern
        match_command_ecdsa = pattern_command_ecdsa.match(line)
        if match_command_ecdsa:
            sig_alg = match_command_ecdsa.group(1)
            kem_alg = match_command_ecdsa.group(2)
            commands.append((sig_alg, kem_alg))
            continue
        
        # Check for connections pattern
        match_connections = pattern_connections.search(line)
        if match_connections:
            num_connections = match_connections.group(1)
            time_seconds = match_connections.group(2).replace('.', ',')
            connections_per_sec = match_connections.group(3).replace('.', ',')
            connections_group.append((num_connections, time_seconds, connections_per_sec))
            
            # Once we have 500 connections, add them to the connections list and reset the group
            if len(connections_group) == 100:
                connections.append(connections_group)
                connections_group = []

    # Add any remaining connections that are less than 50
    if connections_group:
        connections.append(connections_group)

    # Write the filtered data to the output CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the commands values in jumps of three columns
        row = []
        for i, command in enumerate(commands):
            row.extend(command)
            row.extend([''] * (3 - len(command)))  # Adjust for spacing every 3 columns
        csvwriter.writerow(row)

        # Write the header for connections in separate columns
        headers = []
        for i in range(len(connections)):
            headers.extend([f'Group {i+1} Connections', 'Time (s)', 'Connections/User Sec'])
        csvwriter.writerow(headers)

        # Transpose the connections list so that each sublist of 50 connections goes to a new column
        max_length = max(len(group) for group in connections)
        for i in range(max_length):
            row = []
            for group in connections:
                if i < len(group):
                    row.extend(group[i])
                else:
                    row.extend([''] * 3)
            csvwriter.writerow(row)

    print(f"Filtered data has been written to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        
        # Obtiene el nombre base del archivo de entrada (sin la extensión) y añade la extensión .csv
        base_name = os.path.splitext(os.path.basename(input_file_path))[0]
        output_file_path = f"{base_name}.csv"
        
        process_file(input_file_path, output_file_path)

