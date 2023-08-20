#1907. Count Salary Categories

#Question
# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
# - "Low Salary": All the salaries strictly less than $20000.
# - "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# - "High Salary": All the salaries strictly greater than $50000.

# The result table must contain all three categories. If there are no accounts in a category, return 0.
# Return the result table in any order.

# Input: 
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal = sum(accounts.income < 20000)
    avg_sal = sum((accounts.income >=20000)&(accounts.income <=50000))
    high_sal = sum(accounts.income > 50000)

    result=pd.DataFrame({
        'category':['High Salary','Low Salary','Average Salary'],
        'accounts_count':[high_sal,low_sal,avg_sal]
    })

    return result


#!!!!!!!!!!!Doesn't Work!!!!!!!!!!!#
# import pandas as pd
# def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
#     salary_type = np.select([accounts.income < 20000, (accounts.income >=20000)&(accounts.income <=50000),accounts.income > 50000],['Low Salary','Average Salary','High Salary'],np.nan)
#     low_sal = salary_type['Low Salary'].shape(0)
#     avg_sal = salary_type['Average Salary'].shape(0)
#     high_sal = salary_type['High Salary'].shape(0)
#     result=pd.DataFrame({
#         'category':['High Salary','Low Salary','Average Salary'],
#         'accounts_count':[high_sal,avg_sal,low_sal]
#     })
#     return result