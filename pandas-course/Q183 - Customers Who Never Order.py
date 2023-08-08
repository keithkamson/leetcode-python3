import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns={'id':'customerId','name':'Customers'}, inplace = True)
    no_order = pd.merge(customers, orders,how="left", on="customerId")
    no_order['id'].fillna(0,inplace=True)
    no_order_f = no_order[(no_order['id']==0)]
    return no_order_f[["Customers"]]