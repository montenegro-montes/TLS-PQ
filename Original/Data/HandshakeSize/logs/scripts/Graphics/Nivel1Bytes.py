import pandas as pd
import matplotlib.pyplot as plt

FONTSIZE = 26

# Updated data provided by the user
updated_data = {
    'Algorithm': ['rsa-pss-256', 'ed25519', 'falcon512', 'sphincs128f', 'sphincs128s'],
    'X25519_Server': [2064/1024, 668/1024, 2735/1024, 34771/1024, 16263/1024],
    'P-256_Server': [2097/1024, 701/1024, 2758/1024, 34804/1024, 16296/1024],
    'kyber512_Server': [2800/1024, 1404/1024, 3457/1024, 35507/1024, 16999/1024],
    'X25519_Client': [539/1024, 509/1024, 509/1024, 509/1024, 509/1024],
    'P-256_Client': [572/1024, 542/1024, 542/1024, 542/1024, 542/1024],
    'kyber512_Client': [1299/1024, 1269/1024, 1269/1024, 1269/1024, 1269/1024]
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
color5 = '#2a9d8f'  # Dark Green
color6 = '#a7c957'  # Light Green

# Plotting the data with the new colors
bar_width = 0.2
index = range(len(updated_df))

bar1 = ax.bar(index, updated_df['X25519_Server'], bar_width, label='X25519 Server', color=color1)
bar2 = ax.bar(index, updated_df['X25519_Client'], bar_width, bottom=updated_df['X25519_Server'], label='X25519 Client', color=color2)
bar3 = ax.bar([i + bar_width for i in index], updated_df['P-256_Server'], bar_width, label='P-256 Server', color=color3)
bar4 = ax.bar([i + bar_width for i in index], updated_df['P-256_Client'], bar_width, bottom=updated_df['P-256_Server'], label='P-256 Client', color=color4)
bar5 = ax.bar([i + 2*bar_width for i in index], updated_df['kyber512_Server'], bar_width, label='kyber512 Server', color=color5)
bar6 = ax.bar([i + 2*bar_width for i in index], updated_df['kyber512_Client'], bar_width, bottom=updated_df['kyber512_Server'], label='kyber512 Client', color=color6)

# Adding labels, title, and legend
ax.set_xlabel('Signature Algorithm', fontsize=FONTSIZE)
ax.set_ylabel('KBytes', fontsize=FONTSIZE)
ax.set_title('')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels(updated_df['Algorithm'], fontsize=FONTSIZE, rotation=0)

# Place the legend at the top of the plot
#ax.legend(fontsize=16, loc='best')#, bbox_to_anchor=(0.5, 1.15), ncol=1)
ax.legend(fontsize=FONTSIZE, loc='best', title='KEM Algorithm', title_fontsize=FONTSIZE)

# Make the numbers on the axes larger for better readability
ax.tick_params(axis='both', which='major', labelsize=FONTSIZE)

plt.xticks(rotation=0)
plt.tight_layout()

plt.grid(axis = 'y', linestyle='--')

# Save the plot as a PNG file
plt.savefig('Nivel1Bytespng')

plt.show()
