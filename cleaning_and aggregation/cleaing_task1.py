import pandas as pd
from pathlib import Path
#load csv file
df=pd.read_csv(Path(__file__).parent/"orders.csv")


#find missing values

missing=df.isna().sum()

#find duplicates

duplicates=df.duplicated().sum()

print("\nMissing Values:",missing["amount"],"| Duplicates:",duplicates)



#remove duplicates rows
df=df.drop_duplicates()

#fill missing amount with median
median_value=df["amount"].median()
df["amount"]=df["amount"].fillna(median_value)
print("Median used:",median_value)

#change data types

df["amount"]=df["amount"].astype(int)
df["order_id"]=df["order_id"].astype(str)

#groupby and aggregation

result=df.groupby("customer_id").agg(
    total=("amount","sum"),
    orders=("order_id","count")
)
print("customer_id total orders")
for cid,row in result.iterrows():

  print(cid,row["total"],row["orders"])