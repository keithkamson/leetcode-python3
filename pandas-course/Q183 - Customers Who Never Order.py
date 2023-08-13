#Question:
#Write a solution to find all customers who never order anything.

# Input: 
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns={'id':'customerId','name':'Customers'}, inplace = True)
    no_order = pd.merge(customers, orders,how="left", on="customerId")
    no_order['id'].fillna(0,inplace=True)
    no_order_f = no_order[(no_order['id']==0)]
    return no_order_f[["Customers"]]