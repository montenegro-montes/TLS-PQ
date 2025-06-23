import re
import csv
import sys
import os

def process_file(input_file_path, output_file_path):
    # Define the unified regex pattern
    pattern_command = re.compile(r"^Running /opt/oqssa/bin/perftest(?:Mutual|Server)(?:RSA|ECDSA)?\.sh with SIG_ALG=(\w+) and KEM_ALG=([\w-]+)")
    pattern_connections = re.compile(r"(\d+) connections in ([\d\.]+)s; ([\d\.]+) connections/user sec")

    # Open the input file and read the lines
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists to store the filtered data
    commands = []
    connections = []
    current_connections = []

    # Process each line
    for line in lines:
        # Check for the command pattern using the unified regex
        match_command = pattern_command.match(line)
        if match_command:
            if current_connections:
                connections.append(current_connections)  # Add the previous test's connections
                current_connections = []  # Reset for the new group
            sig_alg = match_command.group(1)
            kem_alg = match_command.group(2)
            commands.append((sig_alg, kem_alg))
                
        # Check for connections pattern
        match_connections = pattern_connections.search(line)
        if match_connections:
            num_connections = match_connections.group(1)
            time_seconds = match_connections.group(2).replace('.', ',')
            connections_per_sec = match_connections.group(3).replace('.', ',')
            current_connections.append((num_connections, time_seconds, connections_per_sec))

    # After processing all lines, add the last group of connections if any
    if current_connections:
        connections.append(current_connections)

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

        # Transpose the connections list so that each sublist of connections goes to a new column
        max_length = max(len(group) for group in connections)
        for i in range(max_length):
            row = []
            for group in connections:
                if i < len(group):
                    row.extend(group[i])
                else:
                    row.extend([''] * 3)  # Fill empty if there's no more data in the group
            csvwriter.writerow(row)

        print(f"Filtered data has been written to {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <input_file_path> [output_directory]")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    
    # Si se proporciona un directorio de salida, úsalo; de lo contrario, usa el directorio actual
    if len(sys.argv) == 3:
        output_dir = sys.argv[2]
    else:
        output_dir = os.getcwd()
    
    # Asegúrate de que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)
    
    # Construye la ruta de salida completa
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    output_file_path = os.path.join(output_dir, f"{base_name}.csv")
    
    # Procesa el archivo
    process_file(input_file_path, output_file_path)
    print(f"Process file and save in: {output_file_path}")
