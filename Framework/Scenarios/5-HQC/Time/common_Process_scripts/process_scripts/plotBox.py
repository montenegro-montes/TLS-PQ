import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

# Configurar argparse para recibir el archivo CSV y el directorio de salida
parser = argparse.ArgumentParser(description="Process a CSV and generate a plot.")
parser.add_argument('csv_file', help='Input CSV file')
parser.add_argument('--output_dir', default=os.getcwd(), help='Outuput directory to store plots')
parser.add_argument('--tag', default="--", help='TAG')

args = parser.parse_args()

# Leer el archivo CSV
df = pd.read_csv(args.csv_file, sep=';')

# Extraer la firma y los KEMs de las cabeceras
signature_kem_pairs = df.columns.tolist()  # Lista de todas las columnas
signature, kems = None, []

for col in signature_kem_pairs:
    if ' - ' in col:
        sig, kem = col.split(' - ')
        signature = sig.strip()  # El mismo valor se repetirá en todas, no importa sobrescribir
        kems.append(kem.strip())

# Verificar consistencia
if not signature:
    raise ValueError("No found sign primitive in header.")
if not kems:
    raise ValueError("No found sign primitive in header.")

# Mostrar detalles extraídos
print(f"Sign primitive detected: {signature}")
print(f"KEM primitive detected: {kems}")

# Convertir los valores del DataFrame a flotantes y reorganizar
df = df.replace(',', '.', regex=True).astype(float)
data_by_kem = {kem: df[f"{signature} - {kem}"].values for kem in kems}

# Visualización
fig, ax = plt.subplots(figsize=(14, 8))

# Definir colores distintos para cada KEM
colors = plt.cm.tab20.colors  # Utilizar una paleta de colores distinta
bar_width = 0.5  # Ancho de las barras

positions = []
group_positions = []
current_position = 0

# Crear barras y boxplots
for i, kem in enumerate(kems):
    kem_data = data_by_kem[kem]
    if len(kem_data) > 0:  # Asegurar que haya datos
        # Calcular estadísticos para la barra
        mean = np.mean(kem_data)
        std = np.std(kem_data)

        # Dibujar la barra
        ax.bar(current_position, mean, bar_width, color=colors[i % len(colors)], alpha=0.8)

        # Dibujar el boxplot
        bp = ax.boxplot(kem_data, positions=[current_position], widths=bar_width,
                        patch_artist=True,
                        boxprops=dict(facecolor='none', color='black'),
                        whiskerprops=dict(color='black'),
                        capprops=dict(color='black'),
                        flierprops=dict(marker='+', color=colors[i % len(colors)], alpha=0.5),
                        medianprops=dict(color='red'))
        
        # Guardar posición para las etiquetas del eje X
        positions.append(current_position)
        current_position += 1.5 * bar_width  # Incrementar posición para la siguiente barra

# Configuración de etiquetas y títulos
ax.set_xlabel('KEM Algorithm', fontsize=26, fontweight='bold', labelpad=15)  # puedes ajustar 15 a lo que quieras
ax.set_ylabel('Number of Handshakes', fontsize=26, fontweight='bold')
ax.set_xticks(positions)
ax.tick_params(axis='both', which='major', labelsize=22)
#ax.set_xticklabels(kems, fontsize=20)
kems_wrapped = [
    kem.replace('_', '\n', 1) if '_' in kem else kem
    for kem in kems
]
ax.set_xticklabels(kems_wrapped, fontsize=20)
ax.set_title(f'Performance for Signature Algorithm: {signature}', fontsize=26,fontweight='bold')

# Añadir grid
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Crear el nombre del archivo PNG basado en el nombre del archivo de entrada
input_filename, _ = os.path.splitext(os.path.basename(args.csv_file))  # Extraer solo el nombre base

# Ajustar el diseño
plt.tight_layout()

# Construir la ruta de salida para el gráfico
output_png_file = os.path.join(args.output_dir, f'{input_filename}.grouped_bar_boxplot_{args.tag}.pdf')

# Guardar la gráfica en un archivo PNG
plt.savefig(output_png_file)

print(f"Plot save as: '{output_png_file}'")
