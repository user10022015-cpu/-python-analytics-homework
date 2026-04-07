import pandas as pd
data = { "city" : [ "Kyiv" , "Lviv" , "Odesa" ] , "sales" : [1200, 950, 500] }
df = pd .DataFrame (data)
 print ( "Продажи по городам:" )
print (df)
print ( "Среднее значение:" , df[ "sales" ].mean() )

