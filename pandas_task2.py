import pandas as pd

#load data
df=pd.read_csv("employees.csv")

#Datafram

first_five=df.head()

#df.info()

description=df.describe()


#head() shows the first 5 rows of the data
#info() shows colum name,data typeand non-null counts
#describe shows  count,mean ,min,max of number of column




#select name column

names=df["name"]


#select name and salary together

name_salary=df[["name","salary"]]


#select loc

chennai=df.loc[df["city"]=="Chennai","name"]

#select row& column

data_slice=df.iloc[0:3,1:3]


#fliter sal

high_salary=df[df["salary"]>50000]

#fliter it dep

it_employees=df[df["department"]=="IT"]

print("\nChennai:",", ".join(chennai))
print("Salary above 50000:",len(high_salary),"employees")
print("IT department:",", ".join(it_employees["name"]))



