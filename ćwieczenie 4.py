import pandas as pd

cities = pd.read_csv(r"C:/Users/User/Desktop/GIT REPO/PANDAS/worldcities.csv")
#print(cities.head)
print("##########################################")
print(cities.capital.unique())
print(cities.shape)
print(cities.info())
print((cities.describe()))