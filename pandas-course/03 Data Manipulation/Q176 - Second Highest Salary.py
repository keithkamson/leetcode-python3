# 176. Second Highest Salary

# Question
# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sal = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(sal) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None] })
    result = pd.DataFrame({'SecondHighestSalary': [sal.iloc[1]]})
    return result