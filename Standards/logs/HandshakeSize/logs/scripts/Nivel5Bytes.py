import pandas as pd
import matplotlib.pyplot as plt

# Updated data provided by the user
updated_data = {
    'Algorithm': ['ecdsa-secp521', 'mldsa87', 'falcon1024', 'sphincs256f', 'sphincs256s'],
    'P-521_Server': [1247, 12486, 4957, 100529, 60313],
    'mlkem1024_Server': [2680, 13921, 6390, 101964, 61748],
    'P-521_Client': [640, 610, 610, 610, 610],
    'mlkem1024_Client': [2067, 2037, 2037, 2037, 2037]
}

# Convert all byte values to kilobytes (divide by 1024)
for key in updated_data.keys():
    if key != 'Algorithm':  # Skip the Algorithm column
        updated_data[key] = [x / 1024 for x in updated_data[key]]

# Creating a new DataFrame
updated_df = pd.DataFrame(updated_data)

# Plotting the updated stacked bar chart with larger font sizes
fig, ax = plt.subplots(figsize=(14, 8))

# Define print-friendly colors
color1 = '#004c6d'  # Dark Blue
color2 = '#89c2d9'  # Light Blue
color3 = '#d1495b'  # Dark Red
color4 = '#ffb5a7'  # Light Red

# Plotting the data with the new colors
bar_width = 0.2
index = range(len(updated_df))

bar1 = ax.bar(index, updated_df['P-521_Server'], bar_width, label='P-521 Server', color=color1)
bar2 = ax.bar(index, updated_df['P-521_Client'], bar_width, bottom=updated_df['P-521_Server'], label='P-521 Client', color=color2)
bar3 = ax.bar([i + bar_width for i in index], updated_df['mlkem1024_Server'], bar_width, label='mlkem1024 Server', color=color3)
bar4 = ax.bar([i + bar_width for i in index], updated_df['mlkem1024_Client'], bar_width, bottom=updated_df['mlkem1024_Server'], label='mlkem1024 Client', color=color4)

# Adding labels, title, and legend
ax.set_xlabel('', fontsize=26)
ax.set_ylabel('Kilobytes', fontsize=26)
ax.set_title('')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(updated_df['Algorithm'], fontsize=14, rotation=0)

# Add horizontal grid lines only
ax.grid(True, axis='y', linestyle='--', alpha=0.7)
ax.set_xlabel('Signature Algorithm', fontsize=26)


# Place the legend at the top of the plot
ax.legend(fontsize=16, loc='best', ncol=2, title='KEM algorithm', title_fontsize=16)

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=26)

plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('Level5.single.Exp1.size.png')

plt.show()
