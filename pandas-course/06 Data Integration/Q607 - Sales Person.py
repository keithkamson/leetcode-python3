# 607. Sales Person

# Question 
# Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
# Return the result table in any order.

# Input: 
# SalesPerson table:
# +----------+------+--------+-----------------+------------+
# | sales_id | name | salary | commission_rate | hire_date  |
# +----------+------+--------+-----------------+------------+
# | 1        | John | 100000 | 6               | 4/1/2006   |
# | 2        | Amy  | 12000  | 5               | 5/1/2010   |
# | 3        | Mark | 65000  | 12              | 12/25/2008 |
# | 4        | Pam  | 25000  | 25              | 1/1/2005   |
# | 5        | Alex | 5000   | 10              | 2/3/2007   |
# +----------+------+--------+-----------------+------------+
# Company table:
# +--------+--------+----------+
# | com_id | name   | city     |
# +--------+--------+----------+
# | 1      | RED    | Boston   |
# | 2      | ORANGE | New York |
# | 3      | YELLOW | Boston   |
# | 4      | GREEN  | Austin   |
# +--------+--------+----------+
# Orders table:
# +----------+------------+--------+----------+--------+
# | order_id | order_date | com_id | sales_id | amount |
# +----------+------------+--------+----------+--------+
# | 1        | 1/1/2014   | 3      | 4        | 10000  |
# | 2        | 2/1/2014   | 4      | 5        | 5000   |
# | 3        | 3/1/2014   | 1      | 1        | 50000  |
# | 4        | 4/1/2014   | 1      | 4        | 25000  |
# +----------+------------+--------+----------+--------+

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_orders = orders[orders['com_id'].isin(company[company['name'] == 'RED']['com_id'])]
    no_red_orders = sales_person[~sales_person['sales_id'].isin(red_orders['sales_id'])]
    result = no_red_orders[['name']]
    return result