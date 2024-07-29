import pandas as pd
import matplotlib.pyplot as plt

# Updated data based on the new image provided by the user
updated_data = {
    'Algorithm': ['ecdsa-secp384', 'dilithium3', 'sphincs192f', 'sphincs192s'],
    'P-384_Server': [1101, 9142, 72048, 33102],
    'kyber768_Server': [2093, 10133, 73039, 34093],
    'P-384_Client': [604, 574, 574, 574],
    'kyber768_Client': [1683, 1653, 1653, 1653]
}

# Creating a new DataFrame
updated_df = pd.DataFrame(updated_data)

# Plotting the updated stacked bar chart with larger font sizes
fig, ax = plt.subplots(figsize=(12, 8))

# Define print-friendly colors
color1 = '#004c6d'  # Dark Blue
color2 = '#89c2d9'  # Light Blue
color3 = '#d1495b'  # Dark Red
color4 = '#ffb5a7'  # Light Red

# Plotting the data with the new colors
bar_width = 0.35
index = range(len(updated_df))

bar1 = ax.bar(index, updated_df['P-384_Server'], bar_width, label='P-384 Server', color=color1)
bar2 = ax.bar(index, updated_df['P-384_Client'], bar_width, bottom=updated_df['P-384_Server'], label='P-384 Client', color=color2)
bar3 = ax.bar([i + bar_width for i in index], updated_df['kyber768_Server'], bar_width, label='Kyber768 Server', color=color3)
bar4 = ax.bar([i + bar_width for i in index], updated_df['kyber768_Client'], bar_width, bottom=updated_df['kyber768_Server'], label='Kyber768 Client', color=color4)

# Adding labels, title, and legend
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Bytes', fontsize=16)
ax.set_title('')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(updated_df['Algorithm'], fontsize=14, rotation=0)

# Place the legend at the top of the plot
ax.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=14)

plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('Nivel3Bytes.png')

plt.show()
