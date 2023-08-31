# 1280. Students and Examinations

# Question 
# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.

# Input: 
# Students table:
# +------------+--------------+
# | student_id | student_name |
# +------------+--------------+
# | 1          | Alice        |
# | 2          | Bob          |
# | 13         | John         |
# | 6          | Alex         |
# +------------+--------------+
# Subjects table:
# +--------------+
# | subject_name |
# +--------------+
# | Math         |
# | Physics      |
# | Programming  |
# +--------------+
# Examinations table:
# +------------+--------------+
# | student_id | subject_name |
# +------------+--------------+
# | 1          | Math         |
# | 1          | Physics      |
# | 1          | Programming  |
# | 2          | Programming  |
# | 1          | Physics      |
# | 1          | Math         |
# | 13         | Math         |
# | 13         | Programming  |
# | 13         | Physics      |
# | 2          | Math         |
# | 1          | Math         |
# +------------+--------------+

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_count = examinations[["student_id", "subject_name"]].value_counts().reset_index()
    exam_count = students.merge(subjects, how="cross").merge(exam_count, how="left").fillna(0)
    exam_count = exam_count.rename(columns={"count": "attended_exams"}).sort_values(by=["student_id", "subject_name"])
    result = exam_count[["student_id", "student_name", "subject_name", "attended_exams"]]
    return result