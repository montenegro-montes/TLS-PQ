import subprocess
import os
import argparse
import shutil  # Importar shutil

def run_script_and_process(script_name, log_file, csv_file, logs_dir, output_dir):
    # Ejecutar el script y redirigir la salida a un archivo log
    print(f"Executing script: {script_name}.sh")
    #with open(log_file, 'w') as log:
     #   subprocess.run([f"./docker_scripts/{script_name}.sh"], stdout=log, stderr=subprocess.STDOUT, check=True)


# Configurar argparse para recibir el parámetro 'tag'
parser = argparse.ArgumentParser(description="Processing log files and generating plots.")
parser.add_argument('--tag', required=True, help='Sufix to add to plot files, i.e. "_1ms".')
args = parser.parse_args()

# Directorios específicos
logs_dir = "logs"
scripts_dir = "process_scripts"
docker_scripts = "docker_scripts"
output_dir = "output"
tag = args.tag  # Obtener el 'tag' desde los argumentos

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Crear el directorio de logs si no existe
os.makedirs(logs_dir, exist_ok=True)

# Subdirectorios dentro de output
output_plot = os.path.join(output_dir, "plot")
output_csv = os.path.join(output_dir, "csv")

os.makedirs(output_csv, exist_ok=True)
os.makedirs(output_plot, exist_ok=True)

# Archivos de entrada y salida
logs = ["L1.log", "L3.log", "L5.log"]

logs_dir = "./logs"
output_dir = "./output"
scripts = ["L1", "L3", "L5"]

for script in scripts:
        log_file = f"./docker_scripts/{script}.log"
        csv_file = f"{script}_handshake.csv"
        run_script_and_process(script, log_file, csv_file, logs_dir, output_dir)

csvs = [os.path.join(output_csv, log.replace(".log", ".csv")) for log in logs]
processed_csvs = [csv.replace(".csv", "_handshake.csv") for csv in csvs]

# Paso 0: Mover los archivos .log a logs_dir si no están allí
print("Moving .log files to folder 'logs'...")
for log in logs:
    source_path = os.path.join(docker_scripts, log)
    destination_path = os.path.join(logs_dir, log)
    
    # Mover el archivo solo si no está en la carpeta logs
    if os.path.exists(source_path) and not os.path.exists(destination_path):
        print(f"Moviendo {source_path} -> {destination_path}...")
        shutil.move(source_path, destination_path)
    elif not os.path.exists(source_path):
        print(f"File {source_path} does not exist.")
    else:
        print(f"Fie {log} is in {logs_dir}, it is not necessary to move it.")

# Paso 1: Ejecutar csv_process.py para cada log
print("Processing logs...")
for log, csv_output in zip(logs, csvs):
    log_path = os.path.join(logs_dir, log)
    print(f"Procesando {log_path} -> {csv_output}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "handshakeValues.py"),
        log_path  
    ], check=True)

    # Verificar si se creó un subdirectorio en lugar de un archivo
    if os.path.isdir(csv_output):
        generated_file = os.path.join(csv_output, os.path.basename(csv_output))
        if os.path.exists(generated_file):
            shutil.move(generated_file, csv_output)
            shutil.rmtree(csv_output)  # Eliminar el subdirectorio
        else:
            raise FileNotFoundError(f"Don't found the generated file inside  {csv_output}.")

# Archivos de entrada y salida
csvs = ["L1_handshake.csv", "L3_handshake.csv", "L5_handshake.csv"]
print("Moving  .csv files to 'logs' folder ...")
for csv in csvs:
    source_path = os.path.join(logs_dir, csv)
    destination_path = os.path.join(output_csv, csv)
    
    # Mover el archivo solo si no está en la carpeta logs
    if os.path.exists(source_path):
        print(f"Moving {source_path} -> {destination_path}...")
        shutil.move(source_path, destination_path)
    elif not os.path.exists(source_path):
        print(f"File {source_path} does not exist.")
    else:
        print(f"File  {log} is in  {logs_dir}, it is not necessary to move it.")


# Paso 2: Generar gráficos con plotBox.py para cada CSV procesado
print("\nGenerating plots...")
for processed_csv in processed_csvs:
    print(f"Generating plots to {processed_csv}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "plot.py"),
        processed_csv,
        "--output_dir", output_plot,
        "--tag", tag
    ], check=True)

print("\nProcess complete!")
