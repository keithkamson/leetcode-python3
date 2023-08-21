#1148. Article Views I

#Question:
#Write a solution to find all the authors that viewed at least one of their own articles.

# Input: 
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    own_articles = views[views.author_id == views.viewer_id]
    authors = own_articles.author_id.unique()
    authors = sorted(authors)
    final = pd.DataFrame({'id': authors})
    return final