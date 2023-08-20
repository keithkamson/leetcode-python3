#Question:
#Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.

# Input: 
# Store table:
# +---------+-------------+--------+
# | bill_id | customer_id | amount |
# +---------+-------------+--------+
# | 6       | 1           | 549    |
# | 8       | 1           | 834    |
# | 4       | 2           | 394    |
# | 11      | 3           | 657    |
# | 13      | 3           | 257    |
# +---------+-------------+--------+

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    customers_500 = store[store.amount > 500]
    count_rich = customers_500['customer_id'].nunique()
    result = pd.DataFrame({'rich_count':[count_rich]})
    return result