import pandas as pd

cities = pd.read_csv(r"worldcities.csv")
print(cities.loc[:20])