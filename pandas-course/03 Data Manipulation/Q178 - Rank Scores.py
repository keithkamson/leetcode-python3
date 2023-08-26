# 178. Rank Scores

# Question
# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
# - The scores should be ranked from the highest to the lowest.
# - If there is a tie between two scores, both should have the same ranking.
# - After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

# Return the result table ordered by score in descending order.

# Input: 
# Scores table:
# +----+-------+
# | id | score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    data = scores.sort_values(by='score', ascending=False)
    data['rank'] = data['score'].rank(method='dense', ascending=False)
    result = data[['score','rank']]
    return result