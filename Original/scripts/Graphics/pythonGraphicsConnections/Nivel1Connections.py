import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Algorithm': [
        'rsassa-pss-256', 'ed25519', 'falcon512', 'sphincs128f', 'sphincs128s'
    ],
    'X25519 run1': [1259.41, 882.74, 1290.91, 245.28, 500],
    'X25519 run2': [1282.41, 883.68, 1264.73, 240, 475],
    'X25519 run3': [915, 884.55, 949.88, 255.87, 462.5],
    'X25519 run4': [832.88, 874.25, 1072.97, 268.29, 475],
    'X25519 run5': [957.08, 992.82, 1294.59, 263.46, 633.33],
    'X25519 run6': [931.02, 1048.67, 860.96, 274.52, 450],
    'X25519 run7': [973.27, 1064.57, 1280.2, 255.34, 542.86],
    'X25519 run8': [1008.6, 1054.56, 1246.79, 224.3, 542.86],
    'X25519 run9': [945.45, 1053.11, 1294.54, 231.48, 292.31],
    'X25519 run10': [1139.52, 1058.44, 1245.91, 226.61, 528.57],
    'X25519 run11': [1021.1, 1048.58, 1280.59, 163.41, 475],
    'X25519 run12': [1004.69, 910.48, 1289.71, 230.48, 542.86],
    'X25519 run13': [840.83, 968.56, 1284.56, 267.48, 542.86],
    'X25519 run14': [1038.6, 1051.42, 1266.91, 275.48, 475],
    'X25519 run15': [881.86, 1050.53, 1281.82, 221.15, 487.5],
    'X25519 run16': [959.17, 1033.39, 1289.88, 205.61, 542.86],
    'X25519 run17': [799.55, 1041.61, 1256.56, 211.54, 475],
    'X25519 run18': [1094.39, 1055.6, 1289.68, 197.82, 475],
    'X25519 run19': [1196.7, 1045.47, 1290.15, 200.46, 475],
    'X25519 run20': [1264.56, 1056.58, 1234.87, 197.69, 542.86],
    'X25519 run21': [1224.64, 1049.29, 1059.09, 268.78, 462.5],
    'X25519 run22': [1098.15, 1032.62, 875.58, 267.59, 557.14],
    'X25519 run23': [1089.57, 1054.63, 1322.92, 284.95, 437.5],
    'X25519 run24': [1062.67, 1060.43, 1255.53, 283.82, 475],
    'X25519 run25': [1067.44, 1047.59, 1298.01, 267.45, 542.86],
    'X25519 run26': [1031.19, 1048.06, 1251.2, 272.12, 542.86],
    'X25519 run27': [1027.4, 1048.66, 1289.16, 277.51, 475],
    'X25519 run28': [1128.04, 1061.47, 1297.78, 273.71, 487.5],
    'X25519 run29': [1099.07, 1049.37, 1292.36, 281.34, 414.29],
    'X25519 run30': [1032.27, 1043.72, 1286.52, 277.03, 462.5],
    'X25519 run31': [717.7, 1038.38, 1271.29, 279.43, 475],
    'X25519 run32': [799.11, 1070.4, 1297.27, 281.64, 433.33],
    'X25519 run33': [842.92, 1059.68, 1277.75, 283.41, 475],
    'X25519 run34': [946.12, 1040.54, 1274.88, 279.9, 542.86],
    'X25519 run35': [917.51, 1051.5, 1242.79, 284.39, 487.5],
    'X25519 run36': [959.72, 1061.14, 1242.26, 284.13, 475],
    'X25519 run37': [945.7, 1053.75, 1267.4, 273.33, 542.86],
    'X25519 run38': [862.44, 1061.68, 1281.17, 280.38, 487.5],
    'X25519 run39': [879.82, 1054.17, 1271.01, 281.16, 475],
    'X25519 run40': [794.67, 1038.04, 1286.73, 273.11, 542.86],
    'X25519 run41': [817.27, 1025.09, 1203.12, 282.21, 542.86],
    'X25519 run42': [674.24, 1022.2, 911.86, 281.64, 542.86],
    'X25519 run43': [655.26, 1018.86, 744.22, 275.94, 487.5],
    'X25519 run44': [787.28, 1034.59, 1277.91, 283.57, 475],
    'X25519 run45': [625.11, 1045.21, 1258.37, 284.8, 542.86],
    'X25519 run46': [713.91, 1036.04, 1287.53, 287.32, 475],
    'X25519 run47': [661.3, 1023.26, 1257.79, 281.25, 292.31],
    'X25519 run48': [633.61, 1043.04, 1288.21, 283.65, 487.5],
    'X25519 run49': [542.61, 1002.54, 1255.53, 278.47, 475],
    'X25519 run50': [390.22, 1056.75, 989.86, 264.15, 475],
    'P-256 run1': [608.37, 940.08, 1040.51, 268.22, 422.22],
    'P-256 run2': [508.79, 897.56, 1055.11, 267.44, 475],
    'P-256 run3': [638.43, 877.9, 1034.81, 271.83, 542.86],
    'P-256 run4': [637.21, 993.57, 1057.14, 265.74, 475],
    'P-256 run5': [477.42, 990.08, 1035.66, 265.42, 475],
    'P-256 run6': [615.54, 899.81, 1052.61, 276.08, 433.33],
    'P-256 run7': [590.5, 872.59, 1058.1, 273.24, 475],
    'P-256 run8': [597.65, 906.2, 1065.07, 267.91, 475],
    'P-256 run9': [617.35, 973.29, 1067.99, 269.34, 475],
    'P-256 run10': [588.78, 915.38, 1067.35, 263.83, 475],
    'P-256 run11': [614.88, 905.68, 1037.94, 266.13, 400],
    'P-256 run12': [628.61, 903.86, 1073.53, 265.83, 522.22],
    'P-256 run13': [654.24, 912.89, 1067.43, 269.03, 450],
    'P-256 run14': [645.35, 910.69, 1058.45, 264.12, 480],
    'P-256 run15': [625.28, 920.05, 1067.05, 264.67, 475],
    'P-256 run16': [632.12, 923.52, 1054.35, 268.77, 475],
    'P-256 run17': [654.43, 925.29, 1049.85, 265.33, 462.86],
    'P-256 run18': [652.9, 925.22, 1064.45, 266.23, 475],
    'P-256 run19': [631.3, 924.17, 1049.45, 262.87, 475],
    'P-256 run20': [647.25, 913.62, 1051.7, 261.47, 462.86],
    'P-256 run21': [622.49, 911.39, 1061.92, 265.49, 475],
    'P-256 run22': [612.95, 908.9, 1056.02, 267.54, 462.86],
    'P-256 run23': [639.37, 916.49, 1061.08, 266.5, 475],
    'P-256 run24': [648.41, 921.06, 1060.45, 262.72, 475],
    'P-256 run25': [617.56, 912.95, 1058.71, 262.76, 475],
    'P-256 run26': [614.52, 913.21, 1046.62, 264.7, 475],
    'P-256 run27': [620.48, 913.54, 1049.87, 263.82, 475],
    'P-256 run28': [619.62, 912.46, 1048.94, 263.33, 475],
    'P-256 run29': [628.19, 911.23, 1060.14, 265.37, 475],
    'P-256 run30': [617.52, 915.38, 1046.63, 263.17, 462.86],
    'P-256 run31': [625.74, 918.25, 1067.09, 263.81, 475],
    'P-256 run32': [631.84, 918.35, 1054.94, 264.9, 475],
    'P-256 run33': [614.93, 919.61, 1047.67, 264.29, 475],
    'P-256 run34': [612.11, 920.78, 1061.01, 264.36, 475],
    'P-256 run35': [620.96, 915.65, 1046.87, 263.77, 475],
    'P-256 run36': [617.21, 913.45, 1056.68, 266.01, 475],
    'P-256 run37': [625.64, 914.89, 1047.56, 264.38, 475],
    'P-256 run38': [629.7, 919.03, 1051.56, 263.46, 475],
    'P-256 run39': [628.68, 917.7, 1044.52, 264.47, 475],
    'P-256 run40': [630.33, 915.86, 1067.32, 263.52, 475],
    'P-256 run41': [621.47, 913.56, 1048.67, 264.1, 475],
    'P-256 run42': [624.14, 914.29, 1045.21, 262.86, 475],
    'P-256 run43': [620.5, 914.23, 1061.57, 264.38, 475],
    'P-256 run44': [622.39, 912.65, 1055.41, 263.56, 475],
    'P-256 run45': [620.12, 912.96, 1062.73, 262.69, 475],
    'P-256 run46': [621.57, 914.02, 1055.04, 264.23, 475],
    'P-256 run47': [618.26, 912.21, 1044.84, 265.58, 475],
    'P-256 run48': [621.39, 913.94, 1063.91, 263.21, 475],
    'P-256 run49': [620.56, 912.14, 1062.84, 263.6, 475],
    'P-256 run50': [623.07, 913.86, 1061.12, 264.03, 475],
    'kyber512 run1': [1075, 1192.28, 1106.35, 273.47, 528.57],
    'kyber512 run2': [1164.14, 1163.93, 1092.77, 277.25, 542.86],
    'kyber512 run3': [1023.67, 1203.34, 1108.15, 283.09, 487.5],
    'kyber512 run4': [1199.06, 1174.17, 1102.23, 283.57, 542.86],
    'kyber512 run5': [1104.46, 1195.74, 1118.52, 271.63, 542.86],
    'kyber512 run6': [997.57, 1176.82, 1119.67, 285.51, 542.86],
    'kyber512 run7': [1051.74, 1184.43, 1118.11, 280.38, 542.86],
    'kyber512 run8': [1167.01, 1198.71, 1105.28, 282.69, 542.86],
    'kyber512 run9': [1198.44, 1171.64, 1021.43, 285.92, 487.5],
    'kyber512 run10': [1063.51, 1182, 1010.99, 282.3, 475],
    'kyber512 run11': [1011.76, 1185.5, 1115.61, 282.69, 411.11],
    'kyber512 run12': [893.09, 1186.92, 1096.08, 273.02, 487.5],
    'kyber512 run13': [917.06, 1204.27, 1089.78, 283.09, 542.86],
    'kyber512 run14': [1194.86, 1195.55, 1114.99, 279.81, 542.86],
    'kyber512 run15': [1192.31, 1198.13, 1091.37, 282.3, 485.71],
    'kyber512 run16': [1206.79, 1167.58, 1106.5, 268.37, 200],
    'kyber512 run17': [1222.37, 1177.37, 1083.67, 280.95, 542.86],
    'kyber512 run18': [1185.84, 1187.92, 1119.67, 283.57, 475],
    'kyber512 run19': [1185.71, 1189.15, 1102.66, 288.29, 542.86],
    'kyber512 run20': [1125.45, 1215.38, 986.39, 286.27, 542.86],
    'kyber512 run21': [1093.66, 1190.77, 788.98, 281.9, 475],
    'kyber512 run22': [1323.47, 1197.02, 988.31, 285.78, 542.86],
    'kyber512 run23': [1169.19, 1176.45, 1091.06, 282.13, 542.86],
    'kyber512 run24': [1141.92, 1186.29, 1104.98, 285.29, 557.14],
    'kyber512 run25': [1121.78, 1187.45, 1108.4, 283.57, 542.86],
    'kyber512 run26': [1129, 1170.15, 886.97, 283.01, 475],
    'kyber512 run27': [1181.54, 1200.56, 816.27, 284.13, 542.86],
    'kyber512 run28': [1254.4, 1186.58, 800.64, 282.61, 583.33],
    'kyber512 run29': [1139.41, 1177.72, 900.42, 284.13, 542.86],
    'kyber512 run30': [966.82, 1175.36, 1101.43, 284.39, 542.86],
    'kyber512 run31': [894.84, 1194.42, 1097.78, 282.04, 475],
    'kyber512 run32': [864.57, 1161.88, 974.48, 283.41, 542.86],
    'kyber512 run33': [429.59, 1185.29, 885.03, 281.16, 633.33],
    'kyber512 run34': [510.29, 1159.49, 1108.16, 285.99, 557.14],
    'kyber512 run35': [570.61, 1198.89, 1084.97, 291.54, 542.86],
    'kyber512 run36': [844.29, 1200.56, 1118.11, 288.78, 542.86],
    'kyber512 run37': [936.57, 1195.76, 1093.76, 286.76, 542.86],
    'kyber512 run38': [843.93, 1189.63, 1105.7, 287.86, 312.5],
    'kyber512 run39': [1032.68, 1211.86, 1107.13, 279.33, 475],
    'kyber512 run40': [942.47, 1177.88, 1087.7, 283.9, 542.86],
    'kyber512 run41': [846.45, 1171.01, 1121.37, 288.24, 542.86],
    'kyber512 run42': [1049.1, 1179.82, 1100.61, 282.21, 542.86],
    'kyber512 run43': [934.1, 1197.03, 1096.77, 288.67, 528.57],
    'kyber512 run44': [877.98, 1180.66, 1096.75, 284.13, 542.86],
    'kyber512 run45': [790.09, 1155.93, 1122.96, 250, 542.86],
    'kyber512 run46': [958.41, 1204.87, 1106.75, 287.68, 557.14],
    'kyber512 run47': [1066.36, 1168.5, 1103.86, 290.55, 475],
    'kyber512 run48': [1000, 1113.68, 1099.39, 267.32, 450],
    'kyber512 run49': [740.09, 1036.81, 1102.44, 287.86, 475],
    'kyber512 run50': [892.16, 993.63, 1106.73, 288.24, 542.86]
}


# Convertir a DataFrame
df = pd.DataFrame(data)


# Calcular la media y la desviación estándar
df['X25519_mean'] = df[[col for col in df.columns if col.startswith('X25519')]].mean(axis=1)
df['X25519_std'] = df[[col for col in df.columns if col.startswith('X25519')]].std(axis=1)

df['P-256_mean'] = df[[col for col in df.columns if col.startswith('P-256')]].mean(axis=1)
df['P-256_std'] = df[[col for col in df.columns if col.startswith('P-256')]].std(axis=1)

df['kyber512_mean'] = df[[col for col in df.columns if col.startswith('kyber512')]].mean(axis=1)
df['kyber512_std'] = df[[col for col in df.columns if col.startswith('kyber512')]].std(axis=1)

# Mostrar las estadísticas en la gráfica
fig, ax = plt.subplots(figsize=(14, 8))

# Define print-friendly colors
colors = ['#004c6d', '#d1495b', '#2a9d8f']

# Bar width
bar_width = 0.35
index = np.arange(len(df)) *2


# Crear las barras con errores y centrarlas adecuadamente
bars1 = ax.bar(index - bar_width, df['X25519_mean'], bar_width, yerr=df['X25519_std'], capsize=5, label='X25519', color=colors[0])
bars2 = ax.bar(index, df['P-256_mean'], bar_width, yerr=df['P-256_std'], capsize=5, label='P-256', color=colors[1])
bars3 = ax.bar(index + bar_width, df['kyber512_mean'], bar_width, yerr=df['kyber512_std'], capsize=5, label='kyber512', color=colors[2])


# Adding labels, title, and legend
ax.set_xlabel('Signature Algorithm', fontsize=26)
ax.set_ylabel('Connections', fontsize=26)
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
plt.savefig('./Nivel1Connections.png')

plt.show()