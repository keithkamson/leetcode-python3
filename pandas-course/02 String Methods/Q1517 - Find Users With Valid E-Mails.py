# 1517. Find Users With Valid E-Mails

# Question
# Write a solution to find the users who have valid emails.
# A valid e-mail has a prefix name and a domain where:
# - The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
# - The domain is '@leetcode.com'.

# Return the result table in any order.

# Input: 
# Users table:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_leet = users[users.mail.str.match(r'^[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com')]  
    return valid_leet