# 1741. Find Total Time Spent by Each Employee

# Question
# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
# Return the result table in any order.

# Input: 
# Employees table:
# +--------+------------+---------+----------+
# | emp_id | event_day  | in_time | out_time |
# +--------+------------+---------+----------+
# | 1      | 2020-11-28 | 4       | 32       |
# | 1      | 2020-11-28 | 55      | 200      |
# | 1      | 2020-12-03 | 1       | 42       |
# | 2      | 2020-11-28 | 3       | 33       |
# | 2      | 2020-12-09 | 47      | 74       |
# +--------+------------+---------+----------+

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time_spent'] = employees['out_time'] - employees['in_time']

    result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    result.rename(columns={'event_day': 'day', 'time_spent': 'total_time'}, inplace=True)
    
    return result