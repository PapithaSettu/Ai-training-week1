import pandas as pd
from pathlib import Path
folder=Path(__file__).parent

#load and clean

orders=pd.read_csv(folder/"orders.csv")

orders=orders.drop_duplicates()

orders["amount"]=orders["amount"].fillna(
    orders["amount"].median()
    ).astype(int)
orders["order_id"]=orders["order_id"].astype(str)

#load customers
customers=pd.read_csv(folder/"customers.csv")

#inner join
inner=pd.merge(
    orders,customers,
    on="customer_id",
    how="inner"
)
print("inner join row:",len(inner),"(customer 104 dropped)")

#left join
left=pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"

)
no_orders=left[left["order_id"].isna()]["name"]

print("No orders:",",".join(no_orders))

#outer join
outer=pd.merge(
    orders,customers,
    on="customer_id",
    how="outer"
)
no_customer=outer[outer["name"].isna()]["customer_id"]
print(
    "order without customer:customer_id",
    ",".join(str(i) for i in no_customer)
    )



