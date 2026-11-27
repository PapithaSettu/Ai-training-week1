import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("report/figures",exist_ok=True)

df=pd.read_csv(r"C:\Users\ADMIN\Documents\project\data\employees.csv")

print(df)

#bar chart

avg_salary=df.groupby("department")["salary"].mean()

plt.figure(figsize=(8,5))

bars=plt.bar(avg_salary.index,avg_salary.values)

plt.title("Avearage Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars,fmt="%.2f")
plt.tight_layout()
plt.savefig("report/figures/bar_chart.png")
plt.close()

#histogram

plt.figure(figsize=(8,5))

plt.hist(df["salary"].dropna(),bins=5,edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

#Scatter

plt.figure(figsize=(8,5))

for department in df["department"].dropna().unique():
    dept_data=df[df["department"]==department]

    plt.scatter(
        dept_data["id"],
        dept_data["salary"],
        label=department
    )

    plt.title("employee ID vs Salary")
    plt.xlabel("employee ID")
    plt.ylabel("Salary")
    plt.legend(title="department")

    plt.tight_layout()
    plt.savefig("scatter_plot.png")
    plt.close()

    #line chart

    months=["Jan","Feb","Mar","Apr","May","Jun"]

    sales=[12,15,14,18,22,25]
    plt.plot(
        months,
        sales,
        marker="o",
        label="Monthly Sales"

    )

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()

    plt.tight_layout()
    plt.savefig("line_chart.png")
    plt.close()

    print("all 4 charted successfully")

    # box plot

    plt.figure(figsize=(8,5))
    plt.boxplot(df['salary'].dropna())

    plt.title('Salary Distribution -Box plot')
    plt.xlable('Salary')
    plt.ylable('Salary Amount')

    plt.tight_layout()
    plt.savefig("reports/figures/box_plot.png")
    plt.close()
    

