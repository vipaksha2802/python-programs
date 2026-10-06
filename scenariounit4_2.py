import numpy as np
import pandas as pd

# Create NumPy array of runs scored by players
runs = np.array([5200, 3400, 6100, 2800, 7500, 4900, 5600, 3200, 6800, 4500])

# Calculate average, highest and lowest runs
print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))

# Create Pandas DataFrame
players = pd.DataFrame({
    "Player": ["Player A", "Player B", "Player C", "Player D", "Player E",
               "Player F", "Player G", "Player H", "Player I", "Player J"],
    "Runs": runs
})

print("\nCricket Player Data:")
print(players)

# Display players scoring more than 5000 runs
print("\nPlayers scoring more than 5000 runs:")
print(players[players["Runs"] > 5000])