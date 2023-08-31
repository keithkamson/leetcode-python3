# 586. Customer Placing the Largest Number of Orders

# Question
# Write a solution to find the customer_number for the customer who has placed the largest number of orders.
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.

# Input: 
# Orders table:
# +--------------+-----------------+
# | order_number | customer_number |
# +--------------+-----------------+
# | 1            | 1               |
# | 2            | 2               |
# | 3            | 3               |
# | 4            | 3               |
# +--------------+-----------------+

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    count = orders.groupby('customer_number')['order_number'].count().reset_index()
    result = count[count['order_number'] == count['order_number'].max()][['customer_number']]
    return result