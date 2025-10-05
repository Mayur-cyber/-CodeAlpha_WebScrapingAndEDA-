import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
titanic = sns.load_dataset("titanic")

# Basic info
print("Data Info:")
print(titanic.info())
print("\nSummary Statistics:")
print(titanic.describe())
print("\nMissing Values:")
print(titanic.isnull().sum())

# Survival count
sns.countplot(x="survived", data=titanic)
plt.title("Survival Count")
plt.savefig("survival_count.png")
plt.close()

# Survival by gender
sns.countplot(x="sex", hue="survived", data=titanic)
plt.title("Survival by Gender")
plt.savefig("survival_by_gender.png")
plt.close()

# Age distribution
sns.histplot(titanic["age"].dropna(), kde=True)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.close()
 
# Fare distribution
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

print(" EDA completed & graphs saved")
