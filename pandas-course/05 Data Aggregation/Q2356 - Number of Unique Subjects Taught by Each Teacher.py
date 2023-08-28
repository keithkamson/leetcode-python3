# 2356. Number of Unique Subjects Taught by Each Teacher

# Question:
# Write a solution to calculate the number of unique subjects each teacher teaches in the university.

# Return the result table in any order.

# Input: 
# Teacher table:
# +------------+------------+---------+
# | teacher_id | subject_id | dept_id |
# +------------+------------+---------+
# | 1          | 2          | 3       |
# | 1          | 2          | 4       |
# | 1          | 3          | 3       |
# | 2          | 1          | 1       |
# | 2          | 2          | 1       |
# | 2          | 3          | 1       |
# | 2          | 4          | 1       |
# +------------+------------+---------+

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    subject = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    subject.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return subject