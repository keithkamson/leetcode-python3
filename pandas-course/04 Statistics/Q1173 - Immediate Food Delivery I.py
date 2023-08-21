# 1173. Immediate Food Delivery I

# Question:
# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

# Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.

# Input: 
# Delivery table:
# +-------------+-------------+------------+-----------------------------+
# | delivery_id | customer_id | order_date | customer_pref_delivery_date |
# +-------------+-------------+------------+-----------------------------+
# | 1           | 1           | 2019-08-01 | 2019-08-02                  |
# | 2           | 5           | 2019-08-02 | 2019-08-02                  |
# | 3           | 1           | 2019-08-11 | 2019-08-11                  |
# | 4           | 3           | 2019-08-24 | 2019-08-26                  |
# | 5           | 4           | 2019-08-21 | 2019-08-22                  |
# | 6           | 2           | 2019-08-11 | 2019-08-13                  |
# +-------------+-------------+------------+-----------------------------+

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    same_day_order = delivery[delivery.order_date == delivery.customer_pref_delivery_date].shape[0]
    total_orders = delivery.shape[0]
    same_day_percent = (same_day_order/total_orders)*100
    result = pd.DataFrame({'immediate_percentage':[round(same_day_percent, 2)]})
    return result