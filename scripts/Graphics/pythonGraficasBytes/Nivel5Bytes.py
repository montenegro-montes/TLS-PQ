import pandas as pd
import matplotlib.pyplot as plt

# Updated data provided by the user
updated_data = {
    'Algorithm': ['ed448', 'dilithium5', 'falcon1024', 'falconpadded1024', 'sphincs256f', 'sphincs256s'],
    'P-521_Server': [894, 12422, 4961, 4975, 100529, 60313],
    'kyber1024_Server': [2328, 13857, 6394, 6410, 101964, 61748],
    'P-521_Client': [610, 610, 610, 610, 610, 610],
    'kyber1024_Client': [2037, 2037, 2037, 2037, 2037, 2037]
}

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
bar3 = ax.bar([i + bar_width for i in index], updated_df['kyber1024_Server'], bar_width, label='kyber1024 Server', color=color3)
bar4 = ax.bar([i + bar_width for i in index], updated_df['kyber1024_Client'], bar_width, bottom=updated_df['kyber1024_Server'], label='kyber1024 Client', color=color4)

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
plt.savefig('Nivel5Bytes.png')

plt.show()
