import pandas as pd
import matplotlib.pyplot as plt

# Updated data based on the new provided data
updated_data = {
    'Algorithm': ['rsassa-pss-384','dilithium2'],
    'x448_Server': [2472, 6715 ],
    'x448_Client': [563, 533 ]
}

# Creating a new DataFrame
updated_df = pd.DataFrame(updated_data)

# Plotting the updated stacked bar chart with larger font sizes
fig, ax = plt.subplots(figsize=(10, 6))

# Define print-friendly colors
color1 = '#004c6d'  # Dark Blue
color2 = '#89c2d9'  # Light Blue

# Plotting the data with the new colors
bar_width = 0.35
index = range(len(updated_df))

bar1 = ax.bar(index, updated_df['x448_Server'], bar_width, label='x448 Server', color=color1)
bar2 = ax.bar(index, updated_df['x448_Client'], bar_width, bottom=updated_df['x448_Server'], label='x448 Client', color=color2)

# Adding labels, title, and legend
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Bytes', fontsize=16)
ax.set_title('')
ax.set_xticks(index)
ax.set_xticklabels(updated_df['Algorithm'], fontsize=14, rotation=0)

# Place the legend at the top of the plot
ax.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=14)

plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('Nivel2Bytes.png')

plt.show()
