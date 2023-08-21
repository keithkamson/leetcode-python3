#1683. Invalid Tweets

#Question:
#Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Input: 
# Tweets table:
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    count = tweets[tweets['content'].str.len() > 15]
    return count[['tweet_id']]