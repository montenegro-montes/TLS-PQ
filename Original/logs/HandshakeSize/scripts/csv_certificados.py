import os
import csv

def generate_csv_from_certificates(directory_path, output_csv):
    # Open CSV file for writing
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Filename', 'Size (bytes)'])  # Header row

        # Iterate through files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.crt'):
                file_size = os.path.getsize(file_path)
                csvwriter.writerow([filename, file_size])

    print(f"CSV file '{output_csv}' has been generated successfully.")

if __name__ == "__main__":
    directory_path = input("Enter the directory path containing certificates: ").strip()
    output_csv = input("Enter the output CSV file path: ").strip()

    generate_csv_from_certificates(directory_path, output_csv)
