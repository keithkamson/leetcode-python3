# 511. Game Play Analysis I

# Question
# Write a solution to find the first login date for each player.
# Return the result table in any order.

# Input: 
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-05-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby(['player_id'])['event_date'].min().reset_index()
    result = activity.rename(columns = {'event_date': 'first_login'})
    return result