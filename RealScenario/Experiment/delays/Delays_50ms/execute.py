import subprocess
import os
import argparse

# Configurar argparse para recibir el parámetro 'tag'
parser = argparse.ArgumentParser(description="Procesar archivos log y generar gráficos.")
parser.add_argument('--tag', required=True, help='Sufijo a agregar a los archivos generados de las imagenes, p.ej. "_1ms".')
args = parser.parse_args()

# Directorios específicos
logs_dir = "logs"
scripts_dir = "process_scripts"
output_dir = "output"
tag = args.tag  # Obtener el 'tag' desde los argumentos

# Crear el directorio de salida si no existe
os.makedirs(output_dir, exist_ok=True)

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
