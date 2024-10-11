import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos organizados
data = {
    'Algorithm': ['ecdsa-secp384', 'dilithium3', 'sphincs192f', 'sphincs192s'],
    'P-384_run1': [143.74, 231.61, 128.94, 169.23],
    'P-384_run2': [151.88, 237.45, 131.62, 176.92],
    'P-384_run3': [155.38, 237.52, 127.6, 176.92],
    'P-384_run4': [142.2, 239.31, 129.45, 150],
    'P-384_run5': [114.33, 241.47, 126.5, 164.29],
    'P-384_run6': [126, 237.84, 126.69, 160],
    'P-384_run7': [97.53, 240.18, 129.71, 164.29],
    'P-384_run8': [111.55, 239.38, 130.18, 164.29],
    'P-384_run9': [69.9, 241.73, 128.26, 176.92],
    'P-384_run10': [84.17, 241.36, 128.47, 164.29],
    'P-384_run11': [130.64, 235.74, 129.04, 164.29],
    'P-384_run12': [152.05, 240.55, 125, 176.92],
    'P-384_run13': [136.22, 240.11, 129.82, 176.92],
    'P-384_run14': [122.86, 239.6, 123.64, 176.92],
    'P-384_run15': [148.96, 238.91, 129.45, 164.29],
    'P-384_run16': [154.97, 241.36, 86.22, 164.29],
    'P-384_run17': [140.14, 240.73, 129.35, 169.23],
    'P-384_run18': [155.21, 235.04, 89.72, 153.33],
    'P-384_run19': [156.22, 239.38, 131.62, 164.29],
    'P-384_run20': [123.86, 240.62, 129.45, 169.23],
    'P-384_run21': [102.56, 241.1, 129.09, 146.67],
    'P-384_run22': [89.38, 239.23, 130.04, 164.29],
    'P-384_run23': [96.64, 240.55, 130.18, 164.29],
    'P-384_run24': [117.83, 233.03, 125.44, 164.29],
    'P-384_run25': [50.83, 235.03, 129.35, 164.29],
    'P-384_run26': [66.79, 217.58, 125.98, 164.29],
    'P-384_run27': [83.1, 237.59, 130.88, 171.43],
    'P-384_run28': [118.52, 240.77, 129.35, 176.92],
    'P-384_run29': [89.53, 241.1, 127.14, 164.29],
    'P-384_run30': [93.9, 241.83, 126.15, 135.29],
    'P-384_run31': [137.12, 242.57, 126.79, 157.14],
    'P-384_run32': [134.39, 244.28, 125.81, 164.29],
    'P-384_run33': [145.52, 239.89, 130.29, 171.43],
    'P-384_run34': [126.56, 238.98, 128.73, 164.29],
    'P-384_run35': [118.44, 240.15, 128.42, 169.23],
    'P-384_run36': [119.34, 242.17, 129.93, 171.43],
    'P-384_run37': [136.11, 241.53, 122.65, 164.29],
    'P-384_run38': [133.22, 240.59, 124.56, 164.29],
    'P-384_run39': [124.09, 238.94, 129.82, 164.29],
    'P-384_run40': [127.9, 238.57, 127.34, 176.92],
    'P-384_run41': [126.38, 239.93, 124.82, 169.23],
    'P-384_run42': [143.27, 243.01, 125.89, 164.29],
    'P-384_run43': [154.98, 240.98, 129.82, 153.33],
    'P-384_run44': [148.77, 242.57, 130.66, 176.92],
    'P-384_run45': [142.5, 240.95, 125.35, 176.92],
    'P-384_run46': [140.6, 242.75, 128.32, 160],
    'P-384_run47': [146.82, 241.7, 128.52, 164.29],
    'P-384_run48': [157.12, 241.86, 129.09, 164.29],
    'P-384_run49': [154.83, 242.8, 131.73, 176.92],
    'P-384_run50': [156.07, 242.05, 130.4, 164.29],
    
    'kyber768_run1': [330.89, 1234.78, 233.33, 460],
    'kyber768_run2': [332.91, 1249.9, 238.15, 400],
    'kyber768_run3': [336.08, 1229.66, 237.14, 383.33],
    'kyber768_run4': [314.19, 1170.58, 236.16, 460],
    'kyber768_run5': [317.72, 1252.3, 240.57, 383.33],
    'kyber768_run6': [333.28, 1257.83, 241.38, 383.33],
    'kyber768_run7': [328.48, 1235.56, 238.42, 400],
    'kyber768_run8': [329.67, 1232.57, 241.04, 380],
    'kyber768_run9': [275.67, 1259.03, 242.2, 271.43],
    'kyber768_run10': [274.76, 1244.15, 227.12, 400],
    'kyber768_run11': [307.7, 1248.08, 241.38, 383.33],
    'kyber768_run12': [327.24, 1250.58, 235.03, 383.33],
    'kyber768_run13': [330.41, 1235.48, 240.8, 380],
    'kyber768_run14': [330.65, 1262.45, 232.22, 383.33],
    'kyber768_run15': [322.41, 1262.48, 242.2, 383.33],
    'kyber768_run16': [334.6, 1253.28, 224.19, 460],
    'kyber768_run17': [309.61, 1231.11, 239.43, 400],
    'kyber768_run18': [333.44, 1240.34, 238.64, 383.33],
    'kyber768_run19': [331.03, 1243.21, 238.86, 460],
    'kyber768_run20': [329.54, 1220.86, 239.43, 440],
    'kyber768_run21': [328.39, 1225.67, 206.74, 383.33],
    'kyber768_run22': [318.04, 1235.1, 230.56, 400],
    'kyber768_run23': [328.11, 1246.93, 244.19, 383.33],
    'kyber768_run24': [332.17, 1212.55, 240, 383.33],
    'kyber768_run25': [329.07, 1235.69, 231.49, 383.33],
    'kyber768_run26': [335.6, 1237.07, 231.79, 383.33],
    'kyber768_run27': [332.81, 1253.37, 239.43, 400],
    'kyber768_run28': [313.77, 1239.12, 242.77, 383.33],
    'kyber768_run29': [282.06, 976.45, 237.64, 460],
    'kyber768_run30': [288.16, 942.03, 238.07, 383.33],
    'kyber768_run31': [316.21, 1248.28, 234.48, 460],
    'kyber768_run32': [326.38, 1244.91, 236.57, 480],
    'kyber768_run33': [322.96, 1254.34, 240.8, 383.33],
    'kyber768_run34': [318.91, 1235.56, 240, 460],
    'kyber768_run35': [325.16, 1265.89, 242.77, 400],
    'kyber768_run36': [331.43, 1252.6, 242.2, 383.33],
    'kyber768_run37': [326.97, 1253.76, 233.89, 460],
    'kyber768_run38': [328.01, 1252.69, 235.39, 460],
    'kyber768_run39': [327.24, 1257.95, 238.86, 480],
    'kyber768_run40': [310.79, 1266.08, 238.07, 328.57],
    'kyber768_run41': [293.08, 643.18, 233.71, 460],
    'kyber768_run42': [304.77, 1122.57, 231.28, 460],
    'kyber768_run43': [309.76, 1260.15, 244.44, 383.33],
    'kyber768_run44': [294.68, 1250.19, 236.16, 383.33],
    'kyber768_run45': [292.19, 1238.31, 241.38, 460],
    'kyber768_run46': [289.73, 1257.72, 233.89, 400],
    'kyber768_run47': [318.01, 1265.83, 237.29, 460],
    'kyber768_run48': [321.06, 1247.7, 241.38, 460],
    'kyber768_run49': [331.6, 1233.53, 237.85, 380],
    'kyber768_run50': [326.48, 1223.42, 234.83, 300]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Calcular la media y la desviación estándar
df['P-384_mean'] = df[[col for col in df.columns if col.startswith('P-384')]].mean(axis=1)
df['P-384_std'] = df[[col for col in df.columns if col.startswith('P-384')]].std(axis=1)
df['kyber768_mean'] = df[[col for col in df.columns if col.startswith('kyber768')]].mean(axis=1)
df['kyber768_std'] = df[[col for col in df.columns if col.startswith('kyber768')]].std(axis=1)

# Mostrar las estadísticas en la gráfica
fig, ax = plt.subplots(figsize=(14, 8))
# Define print-friendly colors
colors = ['#004c6d', '#d1495b']

# Bar width
bar_width = 0.35
index = np.arange(len(df))

# Plotting the data
bars1 = ax.bar(index - bar_width/2, df['P-384_mean'], bar_width, label='P-384', yerr=df['P-384_std'], capsize=5, color=colors[0])
bars2 = ax.bar(index + bar_width/2, df['kyber768_mean'], bar_width, label='kyber768', yerr=df['kyber768_std'], capsize=5, color=colors[1])

# Adding labels, title, and legend
ax.set_xlabel('Signature Algorithm', fontsize=26)
ax.set_ylabel('Connections/user sec', fontsize=26)
#ax.set_title('Statistical Analysis of Connections', fontsize=20)
ax.set_xticks(index)
ax.set_xticklabels(df['Algorithm'], fontsize=26, ha='center')

# Place the legend inside the plot with title 'KEM Algorithm'
legend = ax.legend(fontsize=26, loc='best', title='KEM Algorithm', title_fontsize=26)
plt.setp(legend.get_title(), fontsize=26)

# Add grid
plt.grid(axis = 'y', linestyle='--')

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=26)

plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('./Nivel3Connections.png')

plt.show()
