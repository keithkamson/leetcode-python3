# 1050. Actors and Directors Who Cooperated At Least Three Times

# Question 
# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
# Return the result table in any order.

# Input: 
# ActorDirector table:
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')

    filtered_pairs = grouped[grouped['cooperation_count'] >= 3]
    result = filtered_pairs[['actor_id', 'director_id']]
    
    return result