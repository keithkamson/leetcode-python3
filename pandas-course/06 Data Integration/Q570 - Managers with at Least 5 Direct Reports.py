# 570. Managers with at Least 5 Direct Reports

# Question 
# Write a solution to find managers with at least five direct reports.
# Return the result table in any order.

# Input: 
# Employee table:
# +-----+-------+------------+-----------+
# | id  | name  | department | managerId |
# +-----+-------+------------+-----------+
# | 101 | John  | A          | None      |
# | 102 | Dan   | A          | 101       |
# | 103 | James | A          | 101       |
# | 104 | Amy   | A          | 101       |
# | 105 | Anne  | A          | 101       |
# | 106 | Ron   | B          | 101       |
# +-----+-------+------------+-----------+

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_report = employee.groupby('managerId').size().reset_index(name='directReports')
    result = manager_report[manager_report['directReports'] >= 5]
    result = result.merge(employee[['id', 'name']], left_on='managerId', right_on='id', how='inner')
    result = result[['name']]
    
    return result