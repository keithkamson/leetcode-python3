#1757. Recyclable and Low Fat Products

#Question:
#Write a solution to find the ids of products that are both low fat and recyclable.

#Input
# Products table:
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+


import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowfat_recyclable = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return lowfat_recyclable[['product_id']]