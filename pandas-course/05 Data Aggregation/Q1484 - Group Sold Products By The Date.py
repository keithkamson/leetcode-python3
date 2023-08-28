# 1484. Group Sold Products By The Date

# Question:
# Write a solution to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.

# Return the result table ordered by sell_date.

# Input: 
# Activities table:
# +------------+------------+
# | sell_date  | product     |
# +------------+------------+
# | 2020-05-30 | Headphone  |
# | 2020-06-01 | Pencil     |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | Basketball |
# | 2020-06-01 | Bible      |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | T-Shirt    |
# +------------+------------+

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    group = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    
    group.columns = ['sell_date', 'num_sold', 'products']
    group['products'] = group['products'].str.replace(r'(^|,)Mask(,|$)', r'\1Mask\2')
    
    result = group.sort_values(by='sell_date')
    
    return result