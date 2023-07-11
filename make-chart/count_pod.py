import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('./container_cpu_usage_seconds_total.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Calculate the elapsed time in seconds
df['time_elapsed'] = (df['timestamp'] - df['timestamp'].min()).dt.total_seconds().astype(int)

# Group by time_elapsed and count the number of unique pods
df_grouped = df.groupby('time_elapsed').nunique()['pod']

# Create bar plot
plt.figure(figsize=(10, 6))
df_grouped.plot(kind='bar')

# Set labels and font sizes
plt.xlabel('Elapsed Time (s)', fontsize=20)
plt.ylabel('Number of Pods', fontsize=20)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Set tick label font size
plt.tick_params(axis='both', labelsize=15)

# Enable grid
plt.grid()

# Adjust layout
plt.tight_layout()
# Rotate x-axis labels
plt.xticks(rotation=45)

plt.savefig("./count.png")
