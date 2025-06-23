import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
import os
from matplotlib.patches import Patch
from matplotlib.legend_handler import HandlerTuple


# Configurar argparse para recibir parámetros
parser = argparse.ArgumentParser(description="Procesar un archivo CSV y generar una gráfica basada en un algoritmo de firma específico.")
parser.add_argument('csv_file', help='Nombre del archivo CSV de entrada')
parser.add_argument('--output_dir', default=os.getcwd(), help='Directorio de salida para guardar la gráfica')
parser.add_argument('--tag', default="--", help='Elemento diferenciador')

args = parser.parse_args()

csv_file = args.csv_file


# Leer el archivo CSV
df = pd.read_csv(csv_file, sep=',', usecols=['SIG_ALG', 'KEM_ALG', 'Read Bytes', 'Written Bytes'])

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

# Convertir todos los valores de bytes a kilobytes
df['Read Bytes'] = df['Read Bytes'] / 1024
df['Written Bytes'] = df['Written Bytes'] / 1024

# Renombrar columnas para facilitar el manejo
df.rename(columns={'KEM_ALG': 'KEM', 'Read Bytes': 'Server', 'Written Bytes': 'Client'}, inplace=True)

# Obtener el algoritmo de firma (asumimos que es único en toda la columna)
signature_alg = df['SIG_ALG'].iloc[0]

# Obtener los KEM únicos
kems = df['KEM'].unique()

# Definir un vector de colores
colors = ['#004c6d', '#d1495b', '#2a9d8f', '#f4a261', '#e76f51']
kem_colors = {kem: colors[i % len(colors)] for i, kem in enumerate(kems)}


# Crear la gráfica
fig, ax = plt.subplots(figsize=(12, 6))

bar_width = 0.4
x_positions = range(len(kems))

# Lista de handles para la leyenda combinada
legend_items = []

for i, kem in enumerate(kems):
    kem_data = df[df['KEM'] == kem]
    if not kem_data.empty:
        color = kem_colors[kem]
        # Barras apiladas: Server + Client
        ax.bar(
            x_positions[i], kem_data['Server'].values[0], bar_width,
            color=color
        )
        ax.bar(
            x_positions[i], kem_data['Client'].values[0], bar_width,
            bottom=kem_data['Server'].values[0],
            color=color, alpha=0.7
        )

        # Crear entrada doble para leyenda: Server (color normal) + Client (alpha)
        server_patch = Patch(facecolor=color)
        client_patch = Patch(facecolor=color, alpha=0.7)
        legend_items.append(((server_patch, client_patch), f'{kem}    Server - Client'))

# Crear leyenda combinada bien alineada
legend_handles, legend_labels = zip(*legend_items)
ax.legend(
    legend_handles, legend_labels,
    handler_map={tuple: HandlerTuple(ndivide=None, pad=0)},
    title='KEM Algorithm', fontsize=10, title_fontsize=12, loc='best',
    borderpad=1, labelspacing=0.6, handletextpad=0.8
)
# Configurar etiquetas
ax.set_xticks(x_positions)
kems_wrapped = [
    kem.replace('_', '\n', 1) if '_' in kem else kem
    for kem in kems
]
ax.set_xticklabels(kems_wrapped, fontsize=22)
ax.set_xlabel('KEM Algorithm', fontsize=26, fontweight='bold', labelpad=15)  
ax.set_ylabel('Kilobytes Exchanged During Handshake', fontsize=14, fontweight='bold')
ax.set_title(f'Signature Algorithm: {signature_alg}', fontsize=26,fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.tick_params(axis='y', labelsize=16)



input_filename, _ = os.path.splitext(os.path.basename(csv_file))

# Ajustar el diseño y guardar la gráfica
plt.tight_layout()

output_png_file = os.path.join(args.output_dir, f'{input_filename}.single.Exp1.kem.stacked_{args.tag}.pdf')
#output_png_svg = os.path.join(args.output_dir, f'{input_filename}.single.Exp1.kem.stacked_{args.tag}.svg')

plt.savefig(output_png_file)
#plt.savefig(output_png_svg, format="svg")


# Mostrar mensaje de éxito
print(f"Plot generated and stored in: {output_png_file}")