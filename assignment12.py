import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

df = pd.read_csv("customer_churn.csv")

print("First 5 records:")
print(df.head())

# --------------------------------------------------
# 2. Basic information about the dataset
# --------------------------------------------------

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

# --------------------------------------------------
# 3. Check missing values
# --------------------------------------------------

print("\nMissing values in each column:")
print(df.isnull().sum())

# --------------------------------------------------
# 4. Remove duplicate records
# --------------------------------------------------

print("\nNumber of duplicate records:")
print(df.duplicated().sum())

df = df.drop_duplicates()

# --------------------------------------------------
# 5. Handle missing values
# --------------------------------------------------

# Fill missing numerical values with mean
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Summary statistics
# --------------------------------------------------

print("\nSummary Statistics:")
print(df.describe())

# --------------------------------------------------
# 7. Find average monthly charges
# --------------------------------------------------

print("\nAverage Monthly Charges:")
print(np.mean(df["MonthlyCharges"]))

# --------------------------------------------------
# 8. Find average customer tenure
# --------------------------------------------------

print("\nAverage Customer Tenure:")
print(np.mean(df["Tenure"]))

# --------------------------------------------------
# 9. Count customers who churned
# --------------------------------------------------

print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

# --------------------------------------------------
# 10. Churn percentage
# --------------------------------------------------

churn_percentage = df["Churn"].value_counts(normalize=True) * 100

print("\nChurn Percentage:")
print(churn_percentage)

# --------------------------------------------------
# 11. Visualization - Churn Count
# --------------------------------------------------

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 12. Visualization - Monthly Charges
# --------------------------------------------------

plt.hist(df["MonthlyCharges"], bins=10)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 13. Visualization - Tenure
# --------------------------------------------------

plt.hist(df["Tenure"], bins=10)

plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.show()

# --------------------------------------------------
# 14. Churn based on Contract
# --------------------------------------------------

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print("\nChurn based on Contract:")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()

# --------------------------------------------------
# 15. Average Monthly Charges for Churned and
#     Non-Churned Customers
# --------------------------------------------------

average_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage Monthly Charges by Churn:")
print(average_charges)

average_charges.plot(kind="bar")

plt.title("Average Monthly Charges vs Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.show()

# --------------------------------------------------
# 16. Correlation between numerical variables
# --------------------------------------------------

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")
plt.show()