import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🔧 Optional: Create 'plots' folder to save images
SAVE_PLOTS = True
if SAVE_PLOTS:
    os.makedirs("plots", exist_ok=True)

# 📄 Load the Excel file (make sure it's in the same folder or provide full path)
data = pd.read_excel("MAIN DATA.xlsx")

# Convert Churn column for readability
data["Churn"] = data["Churn"].map({0: "No", 1: "Yes"})

# Set seaborn style
sns.set(style="whitegrid")

# 1. Churn Distribution
churn_dist = data["Churn"].value_counts(normalize=True) * 100
print("📊 Churn Distribution (in %):\n", churn_dist)

# 2. Tenure vs Churn
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="Tenure", hue="Churn", multiple="stack", bins=30)
plt.title("Tenure Distribution by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/tenure_vs_churn.png")
plt.show()

# 3. Support Calls vs Churn
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="SupportCalls", hue="Churn", multiple="stack", bins=20)
plt.title("Support Calls Distribution by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/support_calls_vs_churn.png")
plt.show()

# 4. Billing Delay vs Churn
plt.figure(figsize=(8, 5))
sns.histplot(data=data, x="BillingDelay", hue="Churn", multiple="stack", bins=20)
plt.title("Billing Delay Distribution by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/billing_delay_vs_churn.png")
plt.show()

# 5. Plan Type vs Churn
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="PlanType", hue="Churn")
plt.title("Plan Type vs Churn")
plt.xticks(rotation=45)
if SAVE_PLOTS:
    plt.savefig("plots/plan_type_vs_churn.png")
plt.show()

# 6. Agreement Duration vs Churn
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="AgreementDuration", hue="Churn")
plt.title("Agreement Duration vs Churn")
if SAVE_PLOTS:
    plt.savefig("plots/agreement_duration_vs_churn.png")
plt.show()

# 7. Service Usage Rate vs Churn
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x="Churn", y="ServiceUsageRate")
plt.title("Service Usage Rate by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/service_usage_vs_churn.png")
plt.show()

# 8. Total Expenditure vs Churn
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x="Churn", y="TotalExpenditure")
plt.title("Total Expenditure by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/total_expenditure_vs_churn.png")
plt.show()

# 9. Recent Activity vs Churn
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x="Churn", y="RecentActivity")
plt.title("Recent Activity by Churn")
if SAVE_PLOTS:
    plt.savefig("plots/recent_activity_vs_churn.png")
plt.show()

# 10. Gender vs Churn
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="Sex", hue="Churn")
plt.title("Gender vs Churn")
if SAVE_PLOTS:
    plt.savefig("plots/gender_vs_churn.png")
plt.show()

print("✅ All plots generated. Check the 'plots/' folder if saving was enabled.")
