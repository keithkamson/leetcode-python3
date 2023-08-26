#184. Department Highest Salary

#Question
# Write a solution to find employees who have the highest salary in each of the departments.
# Return the result table in any order.

# Input: 
# Employee table:
# +----+-------+--------+--------------+
# | id | name  | salary | departmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# Department table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | IT    |
# | 2  | Sales |
# +----+-------+


import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    data = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    
    highest_salary = data.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    highest_salary = highest_salary.reset_index(drop=True)
    
    result_df = highest_salary[['name_department', 'name_employee', 'salary']]
    result_df.columns = ['Department','Employee', 'Salary']
    
    return result_df