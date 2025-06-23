import subprocess
import os
import argparse
import shutil  # Importar shutil

# Configurar argparse para recibir el parámetro 'tag'
parser = argparse.ArgumentParser(description="Procesar archivos log y generar gráficos.")
parser.add_argument('--tag', required=True, help='Sufijo a agregar a los archivos generados de las imagenes, p.ej. "_1ms".')
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
csvs = [os.path.join(output_csv, log.replace(".log", ".csv")) for log in logs]
print("Archivos CSV generados:")
processed_csvs = [csv.replace(".csv", ".processed.csv") for csv in csvs]

# Paso 0: Mover los archivos .log a logs_dir si no están allí
print("Moviendo archivos .log a la carpeta 'logs'...")
for log in logs:
    source_path = os.path.join(docker_scripts, log)
    destination_path = os.path.join(logs_dir, log)
    
    # Mover el archivo solo si no está en la carpeta logs
    if os.path.exists(source_path) and not os.path.exists(destination_path):
        print(f"Moviendo {source_path} -> {destination_path}...")
        shutil.move(source_path, destination_path)
    elif not os.path.exists(source_path):
        print(f"El archivo {source_path} no existe.")
    else:
        print(f"El archivo {log} ya se encuentra en {logs_dir}, no es necesario moverlo.")

# Paso 1: Ejecutar csv_process.py para cada log
print("Iniciando procesamiento de logs...")
for log, csv_output in zip(logs, csvs):
    log_path = os.path.join(logs_dir, log)
    print(f"Procesando {log_path} -> {csv_output}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "csv_process.py"),
        log_path,
        output_csv  
    ], check=True)

    # Verificar si se creó un subdirectorio en lugar de un archivo
    if os.path.isdir(csv_output):
        generated_file = os.path.join(csv_output, os.path.basename(csv_output))
        if os.path.exists(generated_file):
            shutil.move(generated_file, csv_output)
            shutil.rmtree(csv_output)  # Eliminar el subdirectorio
        else:
            raise FileNotFoundError(f"No se encontró el archivo generado dentro de {csv_output}.")


# Paso 2: Ejecutar transformCSV.py para cada CSV generado
print("\nTransformando archivos CSV...")
for csv in csvs:
    print(f"Transformando {csv}...")
    subprocess.run(["python3", os.path.join(scripts_dir, "transformCSV.py"), csv], check=True)

# Paso 3: Generar gráficos con plotBox.py para cada CSV procesado
print("\nGenerando gráficos...")
for processed_csv in processed_csvs:
    print(f"Generando gráfico para {processed_csv}...")
    subprocess.run([
        "python3",
        os.path.join(scripts_dir, "plotBox.py"),
        processed_csv,
        "--output_dir", output_plot,
        "--tag", tag
    ], check=True)

print("\n¡Proceso completado!")
