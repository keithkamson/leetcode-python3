import pandas as pd

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

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowfat_recyclable = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return lowfat_recyclable[['product_id']]