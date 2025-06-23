import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

# Configurar argparse para recibir el archivo CSV y el directorio de salida
parser = argparse.ArgumentParser(description="Procesar un archivo CSV y generar una gráfica.")
parser.add_argument('csv_file', help='Nombre del archivo CSV de entrada')
parser.add_argument('--output_dir', default=os.getcwd(), help='Directorio de salida para guardar la gráfica')
parser.add_argument('--tag', default="--", help='Elemento diferenciador')

args = parser.parse_args()

# Leer el archivo CSV
df = pd.read_csv(args.csv_file, sep=';')

# Procesar las cabeceras del CSV
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

# Crear el diccionario para agrupar los datos por algoritmo de firma
data_by_signature = {signature: {kem: [] for kem in kems} for signature in signature_algorithms}

# Reorganizar los datos por firma y KEM
for col in df.columns:
    if ' - ' in col:
        signature, kem = col.split(' - ')
        data_by_signature[signature.strip()][kem.strip()] = df[col].values

# Visualización
fig, ax = plt.subplots(figsize=(14, 8))

# Colores para cada KEM
colors = ['#004c6d', '#d1495b', '#2a9d8f', '#f4a261', '#e76f51']
bar_width = 0.4  # Reducir ancho de barras para que todas estén más juntas dentro del grupo
group_spacing = 1  # Espacio entre grupos de firmas
positions = []
group_positions = []
labels = []
current_position = 0

# Crear barras y boxplots
for i, signature in enumerate(signature_algorithms):
    group_positions.append(current_position + (len(kems) - 1) * bar_width / 2)  # Posición central del grupo
    for j, kem in enumerate(kems):
        kem_data = data_by_signature[signature][kem]
        if len(kem_data) > 0:  # Asegurar que haya datos
            # Calcular estadísticos para la barra
            mean = np.mean(kem_data)
            std = np.std(kem_data)

            # Dibujar la barra
            ax.bar(current_position, mean, bar_width, color=colors[j % len(colors)], alpha=0.6,
                   label=kem if i == 0 else "")  # Añadir leyenda solo en la primera iteración

            # Dibujar el boxplot
            bp = ax.boxplot(kem_data, positions=[current_position], widths=bar_width * 0.8,
                            patch_artist=True,
                            boxprops=dict(facecolor='none', color='black'),
                            whiskerprops=dict(color='black'),
                            capprops=dict(color='black'),
                            flierprops=dict(marker='+', color=colors[j % len(colors)], alpha=0.5),
                            medianprops=dict(color='red'))
            
            current_position += bar_width  # Incrementar posición para la siguiente barra
    # Añadir espacio entre los grupos
    current_position += group_spacing - bar_width

# Configuración de etiquetas y títulos
ax.set_xlabel('Signature Algorithm', fontsize=26)
ax.set_ylabel('Connections', fontsize=26)
ax.set_xticks(group_positions)
ax.set_xticklabels(signature_algorithms, fontsize=16)

# Añadir grid
ax.grid(True, axis='y', linestyle='--', alpha=0.7)
# Ajustar el tamaño de la fuente de los ticks
ax.tick_params(axis='both', which='major', labelsize=26)

# Añadir la leyenda
handles = [plt.Line2D([0], [0], color=colors[i], lw=4) for i in range(len(kems))]
ax.legend(handles, kems, title="KEM Algorithm", fontsize=26, title_fontsize=26, loc='upper right')

# Ajustar el diseño
plt.tight_layout()

# Crear el nombre del archivo PNG basado en el nombre del archivo de entrada
input_filename, _ = os.path.splitext(os.path.basename(args.csv_file))  # Extraer solo el nombre base


# Construir la ruta de salida para el gráfico
output_png_file = os.path.join(args.output_dir, f'{input_filename}.grouped_bar_boxplot_{args.tag}.png')

# Guardar la gráfica en un archivo PNG
plt.savefig(output_png_file)

print(f"Gráfica combinada guardada como '{output_png_file}'")
