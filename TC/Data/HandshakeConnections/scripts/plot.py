import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

# Configurar argparse para recibir el archivo CSV
parser = argparse.ArgumentParser(description="Procesar un archivo CSV y generar una gráfica.")
parser.add_argument('csv_file', help='Nombre del archivo CSV de entrada')
args = parser.parse_args()

# Leer el archivo CSV
df = pd.read_csv(args.csv_file, sep=';')

# Procesar las cabeceras del CSV
# Reemplazar "RSA-3072" por "rsassa-pss-256"
#df.columns = [col.replace('RSA-3072', 'rsassa-pss-256') for col in df.columns]
df.columns = [col.replace('sphincssha2128fsimple', 'sphincs128f') for col in df.columns]
df.columns = [col.replace('sphincssha2128ssimple', 'sphincs128s') for col in df.columns]

df.columns = [col.replace('sphincssha2192fsimple', 'sphincs192f') for col in df.columns]
df.columns = [col.replace('sphincssha2192ssimple', 'sphincs192s') for col in df.columns]

df.columns = [col.replace('sphincssha2256fsimple', 'sphincs256f') for col in df.columns]
df.columns = [col.replace('sphincssha2256ssimple', 'sphincs256s') for col in df.columns]





# Extraer los algoritmos de firma y KEM de las cabeceras
signature_algorithms = []
kems = []
for col in df.columns:
    if ' - ' in col:  # Verifica que la columna siga el formato esperado
        signature, kem = col.split(' - ')
        if signature not in signature_algorithms:
            signature_algorithms.append(signature.strip())
        if kem not in kems:
            kems.append(kem.strip())

# Mostrar los algoritmos de firma y KEM detectados
print(f"Algoritmos de firma detectados: {signature_algorithms}")
print(f"KEMs detectados: {kems}")

# Convertir los valores de las columnas a flotantes
df = df.replace(',', '.', regex=True).astype(float)

# Crear el diccionario data
data = {
    'Algorithm': signature_algorithms
}

# Añadir los datos de las columnas al diccionario data
for kem_name in kems:
    columns = [col for col in df.columns if col.endswith(kem_name)]
    for i in range(len(df)):
        data[f'{kem_name} run{i + 1}'] = df.loc[i, columns].tolist()

df_data = pd.DataFrame(data)

# Calcular la media y la desviación estándar
def calculate_stats(df, columns):
    return df[columns].mean(axis=1), df[columns].std(axis=1)

# Calcular las estadísticas para cada KEM
for kem_name in kems:
    mean, std = calculate_stats(df_data, [col for col in df_data.columns if col.startswith(kem_name)])
    df_data[f'{kem_name}_mean'] = mean
    df_data[f'{kem_name}_std'] = std

# Visualización
fig, ax = plt.subplots(figsize=(14, 8))

# Definir colores y ancho de las barras
colors = ['#004c6d', '#d1495b', '#2a9d8f']
bar_width = 0.4
index = np.arange(len(df_data)) * 2

# Crear las barras con errores para cada KEM
for i, (kem_name, color) in enumerate(zip(kems, colors)):
    bars = ax.bar(index + i * bar_width - bar_width, 
                  df_data[f'{kem_name}_mean'], 
                  bar_width, 
                  yerr=df_data[f'{kem_name}_std'], 
                  capsize=5, 
                  label=kem_name, 
                  color=color)

# Configuración de la gráfica
ax.set_xlabel('Signature Algorithm', fontsize=26)
ax.set_ylabel('Connections/user sec', fontsize=26)
ax.set_xticks(index)
ax.set_xticklabels(df_data['Algorithm'], fontsize=18, ha='center')

# Añadir título y leyenda
legend = ax.legend(fontsize=26, loc='upper left', bbox_to_anchor=(0.65, 0.95), title='KEM Algorithm')
plt.setp(legend.get_title(), fontsize=26)

# Añadir grid
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Ajustar el tamaño de la fuente de los ticks
ax.tick_params(axis='both', which='major', labelsize=26)

# Ajustar el diseño y guardar la gráfica
plt.tight_layout()

# Crear el nombre del archivo PNG basado en el nombre del archivo de entrada
input_filename, _ = os.path.splitext(args.csv_file)
output_png_file = f'{input_filename}.connections.png'

# Guardar la gráfica en un archivo PNG
plt.savefig(output_png_file)

# Mostrar la gráfica
#plt.show()

print(f"Gráfica guardada como '{output_png_file}'")