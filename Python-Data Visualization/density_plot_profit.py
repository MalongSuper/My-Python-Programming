# Density Plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame
df = pd.read_csv('datasets/CompanyABCProfit.csv')

# Set the style for the plot
sns.set(style="whitegrid")

# Create a Density Plot for 'Profit (Rs \'000)'
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Profit(Rs000)'], shade=True, color='blue', alpha=0.6)

# Add labels and title
plt.title("Density Plot for Profit(Rs000) Over the Years", fontsize=16)
plt.xlabel("Profit(Rs000)", fontsize=12)
plt.ylabel("Density", fontsize=12)


# Display the plot
plt.show()
