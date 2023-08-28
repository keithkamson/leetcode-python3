# 596. Classes More Than 5 Students

# Question:
# Write a solution to find all the classes that have at least five students.
# Return the result table in any order.

# Input: 
# Courses table:
# +---------+----------+
# | student | class    |
# +---------+----------+
# | A       | Math     |
# | B       | English  |
# | C       | Math     |
# | D       | Biology  |
# | E       | Math     |
# | F       | Computer |
# | G       | Math     |
# | H       | Math     |
# | I       | Math     |
# +---------+----------+

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    subject = courses.groupby('class')['student'].count().reset_index()
    result = subject[subject['student'] >= 5][["class"]]
    return result