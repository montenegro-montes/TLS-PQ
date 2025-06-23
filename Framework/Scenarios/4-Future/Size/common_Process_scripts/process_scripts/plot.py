import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
import os
from matplotlib.patches import Patch
from matplotlib.legend_handler import HandlerTuple

# Configurar argparse para recibir el archivo CSV y el directorio de salida
parser = argparse.ArgumentParser(description="Procesar un archivo CSV y generar una gráfica.")
parser.add_argument('csv_file', help='Nombre del archivo CSV de entrada')
parser.add_argument('--output_dir', default=os.getcwd(), help='Directorio de salida para guardar la gráfica')
parser.add_argument('--tag', default="--", help='Elemento diferenciador')

args = parser.parse_args()

csv_file = args.csv_file

# Leer el archivo CSV
df = pd.read_csv(args.csv_file, sep=',', usecols=['SIG_ALG', 'KEM_ALG', 'Read Bytes', 'Written Bytes'])

# Procesar las cabeceras del CSV

df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2128fsimple', 'sphincs128f') 
df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2128ssimple', 'sphincs128s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2192fsimple', 'sphincs192f') 
df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2192ssimple', 'sphincs192s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2256fsimple', 'sphincs256f') 
df['SIG_ALG'] = df['SIG_ALG'].replace('sphincssha2256ssimple', 'sphincs256s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('p256_sphincssha2128ssimple', 'p256_sphincs128s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('p256_sphincssha2128fsimple', 'p256_sphincs128f') 

df['SIG_ALG'] = df['SIG_ALG'].replace('p384_sphincssha2192ssimple', 'p384_sphincs192s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('p384_sphincssha2192fsimple', 'p384_sphincs192f') 

df['SIG_ALG'] = df['SIG_ALG'].replace('p521_sphincssha2256ssimple', 'p521_sphincs256s') 
df['SIG_ALG'] = df['SIG_ALG'].replace('p521_sphincssha2256fsimple', 'p521_sphincs256f') 

df['SIG_ALG'] = df['SIG_ALG'].replace('CROSSrsdpg128balanced', 'cross128') 
df['SIG_ALG'] = df['SIG_ALG'].replace('CROSSrsdpg192balanced', 'cross192') 
df['SIG_ALG'] = df['SIG_ALG'].replace('CROSSrsdpg256balanced', 'cross256') 

# Convertir todos los valores de bytes a kilobytes (dividir por 1024)
df['Read Bytes'] = df['Read Bytes'] / 1024
df['Written Bytes'] = df['Written Bytes'] / 1024

# Renombrar columnas para facilitar el manejo
df.rename(columns={'KEM_ALG': 'KEM', 'Read Bytes': 'Server', 'Written Bytes': 'Client'}, inplace=True)

# Obtener los algoritmos de firma y KEM únicos
signature_algorithms = df['SIG_ALG'].unique()
kems = df['KEM'].unique()

# Definir un vector de colores
colors = ['#004c6d', '#d1495b', '#2a9d8f', '#f4a261', '#e76f51']
kem_colors = {kem: colors[i % len(colors)] for i, kem in enumerate(kems)}

# Crear la gráfica de barras agrupadas y apiladas
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.4  # Ancho de cada barra
spacing = 0.8  # Espaciado entre grupos
x_positions = []  # Posiciones para las barras
labels = []  # Etiquetas para el eje x

# Lista de handles para la leyenda combinada
legend_items = []

current_x = 0
legend = True
for signature in signature_algorithms:
    subset = df[df['SIG_ALG'] == signature]
    
    for i, kem in enumerate(kems):
        kem_data = subset[subset['KEM'] == kem]
        if not kem_data.empty:
            color = kem_colors[kem]
            # Graficar Server
            ax.bar(
                current_x + i * bar_width, kem_data['Server'].values[0], bar_width,
                label=f'{kem} Server' if current_x == 0 else None,
                color=color
            )
            # Graficar Client apilado sobre Server
            ax.bar(
                current_x + i * bar_width, kem_data['Client'].values[0], bar_width,
                bottom=kem_data['Server'].values[0],
                label=f'{kem} Client' if current_x == 0 else None,
                color=color, alpha=0.7
            )

            if legend:
                # Crear entrada doble para leyenda: Server (color normal) + Client (alpha)
                server_patch = Patch(facecolor=color)
                client_patch = Patch(facecolor=color, alpha=0.7)
                legend_items.append(((server_patch, client_patch), f'{kem}    Server - Client'))
    
    legend = False
    x_positions.append(current_x + ((len(kems) - 1) * bar_width) / 2)
    labels.append(signature)
    current_x += len(kems) * bar_width + spacing

# Crear leyenda combinada bien alineada
legend_handles, legend_labels = zip(*legend_items)
ax.legend(
    legend_handles, legend_labels,
    handler_map={tuple: HandlerTuple(ndivide=None, pad=0)},
    title='KEM Algorithm', fontsize=12, title_fontsize=15, loc='best',
    borderpad=1, labelspacing=0.8, handletextpad=1.5
)

# Configurar etiquetas y leyenda
ax.set_xticks(x_positions)
kems_wrapped = [
    kem.replace('_', '\n', 1) if '_' in kem else kem
    for kem in labels
]
ax.set_xticklabels(kems_wrapped, fontsize=22, ha='center')
ax.set_ylabel('Kilobytes Exchanged During Handshake', fontsize=18, fontweight='bold')
ax.set_xlabel('KEM Algorithm', fontsize=26, fontweight='bold', labelpad=15)  
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.tick_params(axis='y', labelsize=16)

#ax.tick_params(axis='both', which='major', labelsize=16)

input_filename, _ = os.path.splitext(os.path.basename(csv_file))

# Ajustar el diseño para centrar las etiquetas
plt.tight_layout()

# Construir la ruta de salida para el gráfico
output_png_file = os.path.join(args.output_dir, f'{input_filename}.grouped_bar_boxplot_{args.tag}.pdf')

# Guardar la gráfica como PNG
plt.savefig(output_png_file)

# Mostrar la gráfica
# plt.show()