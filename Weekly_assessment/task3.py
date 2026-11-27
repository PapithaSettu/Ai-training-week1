import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))
FIG = os.path.join(ROOT, "reports", "figures")
os.makedirs(FIG, exist_ok=True)



#  PART 1: NumPy 
marks = np.array([[78, 85, 90],
                  [65, 70, 72],
                  [88, 92, 95],
                  [55, 60, 58]])         
#print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
#print("Subject averages:", marks.mean(axis=0))

# broadcasting
grace = marks + 5                           
#print("After grace marks:\n", grace)

weights = np.array([0.5, 0.3, 0.2])
#print("Weighted scores:", np.dot(marks, weights))

 #Pandas basics
emp = pd.read_csv(os.path.join(ROOT, "employees.csv"))
#emp.info()
#print(emp.describe())
#print(emp.loc[0, "name"])                   
#print(emp.iloc[0:3, 1:4])                   
#print(emp[emp["salary"] > 50000])           

# departments.csv + cleaning 
dept_path = os.path.join(BASE, "departments.csv")
pd.DataFrame({
    "department": ["Sales", "HR", "IT", "Finance", "Admin"],
    "head": ["Ravi", "Lakshmi", "Kumar", "Sneha", "Vimal"],
    "budget": [500000, 400000, 900000, 600000, 200000],
}).to_csv(dept_path, index=False)          

dirty_path = os.path.join(ROOT, "employees_dirty.csv")
df = pd.read_csv(dirty_path)
#print("Missing before:\n", df.isna().sum())
df = df.drop_duplicates()
df["salary"] = df["salary"].fillna(df["salary"].median())
df["salary"] = df["salary"].astype(int)     
#print("Rows after cleaning:", len(df))

# PART 4: groupby + merge 
stats = df.groupby("department").agg(
    headcount=("id", "count"),
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
)
#print(stats)

order = ["Sales", "HR", "IT", "Finance"]
print("Headcount:", " | ".join(f"{d} {stats.loc[d, 'headcount']}" for d in order))

depts = pd.read_csv(dept_path)
inner = pd.merge(df, depts, on="department", how="inner")
left = pd.merge(df, depts, on="department", how="left")
outer = pd.merge(df, depts, on="department", how="outer")
#print("Inner rows:", len(inner), "| Left rows:", len(left), "| Outer rows:", len(outer))

no_emp = outer[outer["id"].isna()]["department"].tolist()
print("Outer join - departments with no employees:", no_emp)

# Chart
COLOR = "#2E86AB"

# 1 Bar
plt.figure(figsize=(8, 5))
plt.bar(stats.index, stats["avg_salary"], color=COLOR, label="Average salary")
plt.title("Average Salary by Department")
plt.xlabel("Department"); plt.ylabel("Salary (INR)")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(FIG, "bar_chart.png")); plt.close()

# 2 Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=6, color=COLOR, edgecolor="white", label="Employees")
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)"); plt.ylabel("Number of employees")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(FIG, "histogram.png")); plt.close()

# 3 Scatter (experience column illa, so id use pannirukken)
plt.figure(figsize=(8, 5))
plt.scatter(df["id"], df["salary"], color=COLOR, label="Employee")
plt.title("Salary vs Employee ID")
plt.xlabel("Employee ID"); plt.ylabel("Salary (INR)")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(FIG, "scatter_plot.png")); plt.close()

# 4 Line (sorted salary)
s = df["salary"].sort_values().reset_index(drop=True)
plt.figure(figsize=(8, 5))
plt.plot(s.index + 1, s.values, marker="o", color=COLOR, label="Salary")
plt.title("Salaries in Ascending Order")
plt.xlabel("Employee rank (lowest to highest)"); plt.ylabel("Salary (INR)")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(FIG, "line_chart.png")); plt.close()

#print("Charts saved to reports/figures")

