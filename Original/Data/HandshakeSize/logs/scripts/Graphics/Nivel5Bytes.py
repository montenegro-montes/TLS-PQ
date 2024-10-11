import pandas as pd
import matplotlib.pyplot as plt

FONTSIZE = 26

# Updated data provided by the user
updated_data = {
    'Algorithm': ['ed448', 'dilithium5', 'falcon1024', 'sphincs256f', 'sphincs256s'],
    'P-521_Server': [894/1024, 12422/1024, 4961/1024, 100529/1024, 60313/1024],
    'kyber1024_Server': [2328/1024, 13857/1024, 6394/1024, 101964/1024, 61748/1024],
    'P-521_Client': [610/1024, 610/1024, 610/1024, 610/1024, 610/1024],
    'kyber1024_Client': [2037/1024, 2037/1024, 2037/1024, 2037/1024, 2037/1024]
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
bar_width = 0.35
index = range(len(updated_df))

bar1 = ax.bar(index, updated_df['P-521_Server'], bar_width, label='P-521 Server', color=color1)
bar2 = ax.bar(index, updated_df['P-521_Client'], bar_width, bottom=updated_df['P-521_Server'], label='P-521 Client', color=color2)
bar3 = ax.bar([i + bar_width for i in index], updated_df['kyber1024_Server'], bar_width, label='kyber1024 Server', color=color3)
bar4 = ax.bar([i + bar_width for i in index], updated_df['kyber1024_Client'], bar_width, bottom=updated_df['kyber1024_Server'], label='kyber1024 Client', color=color4)

# Adding labels, title, and legend
ax.set_xlabel('Signature Algorithm', fontsize=FONTSIZE)
ax.set_ylabel('KBytes', fontsize=FONTSIZE)
ax.set_title('')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(updated_df['Algorithm'], fontsize=FONTSIZE, rotation=0)

# Place the legend at the top of the plot
#ax.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
ax.legend(fontsize=FONTSIZE, loc='best', title='KEM Algorithm', title_fontsize=FONTSIZE)

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)

plt.xticks(rotation=0)
plt.tight_layout()

plt.grid(axis = 'y', linestyle='--')

# Save the plot as a PNG file
plt.savefig('Nivel5Bytes.png')

plt.show()
