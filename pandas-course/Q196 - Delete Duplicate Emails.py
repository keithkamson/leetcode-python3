#Question:
#Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
# For Pandas users, please note that you are supposed to modify Person in place.

# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.


# Input: 
# Person table:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com | 
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+


import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = 'id', ascending = True, inplace = True)
    person.drop_duplicates(subset='email', keep = 'first', inplace = True)