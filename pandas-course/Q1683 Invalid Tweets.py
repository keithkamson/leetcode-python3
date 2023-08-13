import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    count = tweets[tweets['content'].str.len() > 15]
    return count[['tweet_id']]