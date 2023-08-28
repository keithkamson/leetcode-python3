# 1693. Daily Leads and Partners

# Question:
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
# Return the result table in any order.

# DailySales table:
# +-----------+-----------+---------+------------+
# | date_id   | make_name | lead_id | partner_id |
# +-----------+-----------+---------+------------+
# | 2020-12-8 | toyota    | 0       | 1          |
# | 2020-12-8 | toyota    | 1       | 0          |
# | 2020-12-8 | toyota    | 1       | 2          |
# | 2020-12-7 | toyota    | 0       | 2          |
# | 2020-12-7 | toyota    | 0       | 1          |
# | 2020-12-8 | honda     | 1       | 2          |
# | 2020-12-8 | honda     | 2       | 1          |
# | 2020-12-7 | honda     | 0       | 1          |
# | 2020-12-7 | honda     | 1       | 2          |
# | 2020-12-7 | honda     | 2       | 1          |
# +-----------+-----------+---------+------------+

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id': 'nunique', 'partner_id': 'nunique'}).reset_index()
    result.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']
    return result