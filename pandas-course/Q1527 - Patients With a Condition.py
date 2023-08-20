#1527. Patients With a Condition

#Question
# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
# Return the result table in any order.

# Input: 
# Patients table:
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 1          | Daniel       | YFEV COUGH   |
# | 2          | Alice        |              |
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# | 5          | Alain        | DIAB201      |
# +------------+--------------+--------------+

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    condition = patients[patients.conditions.str.contains(r'\bDIAB1')]
    result = condition[['patient_id','patient_name', 'conditions']]
    return result