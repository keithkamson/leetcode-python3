#595. Big Countries

#Question:
# A country is big if:
# - it has an area of at least three million (i.e., 3000000 km2), or
# - it has a population of at least twenty-five million (i.e., 25000000).


# Input:
# World table:
# +-------------+-----------+---------+------------+--------------+
# | name        | continent | area    | population | gdp          |
# +-------------+-----------+---------+------------+--------------+
# | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
# | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
# | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
# | Andorra     | Europe    | 468     | 78115      | 3712000000   |
# | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
# +-------------+-----------+---------+------------+--------------+

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country = world[(world.area >= 3000000) | (world.population >= 25000000)]
    return big_country[['name','area','population']]
