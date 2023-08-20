#1667. Fix Names in a Table

#Question:
# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# Return the result table ordered by user_id.

# Input: 
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.name = users.name.str.capitalize()

    result = users.sort_values(by='user_id', ascending=True)

    return result