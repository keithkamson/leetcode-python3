# 1378. Replace Employee ID With The Unique Identifier

# Question 
# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
# Return the result table in any order.

# Input: 
# Employees table:
# +----+----------+
# | id | name     |
# +----+----------+
# | 1  | Alice    |
# | 7  | Bob      |
# | 11 | Meir     |
# | 90 | Winston  |
# | 3  | Jonathan |
# +----+----------+
# EmployeeUNI table:
# +----+-----------+
# | id | unique_id |
# +----+-----------+
# | 3  | 1         |
# | 11 | 2         |
# | 90 | 3         |
# +----+-----------+

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(employee_uni, on='id', how='left')
    result = merged[['unique_id','name']]
    return result