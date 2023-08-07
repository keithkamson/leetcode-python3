import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    own_articles = views[views.author_id == views.viewer_id]
    authors = own_articles.author_id.unique()
    authors = sorted(authors)
    final = pd.DataFrame({'id': authors})
    return final