import pandas as pd
data = { "city" : [ "Kyiv" , "Lviv" , "Odesa" ] , "sales" : [1200, 950, 500] }
df = pd .DataFrame (data)
print ( "Продажи по городам (временная версия):" )
print (df)
average_sales = df [ "sales" ] .mean ()
 print ( "Среднее значение:" , average_sales)
print ( "Это средний уровень продаж по трем городам" )
