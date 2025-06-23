import pandas as pd
import argparse
import os

# Configurar argparse para recibir el archivo CSV
parser = argparse.ArgumentParser(description="Process a CSV file and create other with columns 'Connections/User Sec'.")
parser.add_argument('input_file', help='CSV filename input')
parser.add_argument('output_file', nargs='?', help='CSV filename output (optional)')

args = parser.parse_args()

# Si no se proporciona un archivo de salida, generar un nombre basado en el archivo de entrada
if not args.output_file:
    input_filename, input_ext = os.path.splitext(args.input_file)
    args.output_file = f'{input_filename}.processed{input_ext}'

# Cargar el archivo CSV
# Nota: Usamos header=None porque las cabeceras están en las dos primeras filas
df = pd.read_csv(args.input_file, sep=',', header=None)

# Mostrar las primeras filas para verificar el contenido
print("First DataFrame rows:")
print(df.head())

# Extraer las cabeceras desde la primera fila (que contiene algoritmo de firma y KEM)
header_row = df.iloc[0].astype(str)  # La primera fila contiene "algoritmo_firma, KEM"
data_headers = df.iloc[1].astype(str)  # La segunda fila contiene nombres de datos adicionales (si es necesario)

# Crear un diccionario para mapear Algoritmo de Firma -> KEM (incluyendo todos los pares)
kem_to_columns = {}
for i in range(0, len(header_row), 3):
    # Verificamos que las posiciones de Algoritmo de Firma y KEM no estén vacías
    signature_algorithm = header_row[i].strip() if pd.notna(header_row[i]) else None
    kem_algorithm = header_row[i+1].strip() if pd.notna(header_row[i+1]) else None
    
    if signature_algorithm and kem_algorithm:
        # Agregamos cada par de Algoritmo de Firma y KEM al diccionario, junto con su respectiva columna
        #column_index = i + 2  # La columna "Connections/User Sec" está en la tercera posición de cada bloque
        column_index = i   # La columna "Connections" está en la primera posición de cada bloque
        column_name = f"{signature_algorithm} - {kem_algorithm}"
        
        if column_name not in kem_to_columns:
            kem_to_columns[column_name] = [column_index]
        else:
            kem_to_columns[column_name].append(column_index)

# Crear un nuevo DataFrame con todas las columnas relevantes
ordered_columns = []
ordered_column_names = []

for name, columns in kem_to_columns.items():
    ordered_columns.extend(columns)
    ordered_column_names.extend([name] * len(columns))

# Crear el DataFrame final con las columnas ordenadas
df_connections_user_sec = df.iloc[2:, ordered_columns]

# Reemplazar los encabezados de las columnas con el formato 'Algoritmo de Firma - KEM'
df_connections_user_sec.columns = ordered_column_names

# Mostrar el DataFrame final antes de guardarlo
print("\nDataFrame final (first 5 rows):")
print(df_connections_user_sec.head())

# Guardar el DataFrame resultante en un nuevo archivo CSV
df_connections_user_sec.to_csv(args.output_file, sep=';', index=False)

print(f"New CSV created: '{args.output_file}'")