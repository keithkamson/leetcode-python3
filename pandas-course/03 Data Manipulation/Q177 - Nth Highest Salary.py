# 177. Nth Highest Salary

# Question
# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sal = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if N > len(sal):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    result = pd.DataFrame({'Nth Highest Salary': [sal.iloc[N - 1]]})
    return result