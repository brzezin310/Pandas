import pandas as pd
#lista = [[1,4,2,4,1],[5,2,5,1,5]] #lista liczb do dataframe
lista = {'Imię':['Adam','Gabi','Kinga'],'Wiek':[28,21,21]}
dane = pd.DataFrame(lista)
print(dane)

s = pd.Series([11,22,33,44])
print(pd.DataFrame(s))