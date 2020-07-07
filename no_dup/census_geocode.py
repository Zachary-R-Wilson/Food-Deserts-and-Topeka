import censusgeocode as cg
import pandas as pd 

csv_list=['bakery.csv','home_goods_store.csv','supermarket.csv',
'convenience_store.csv','liquor_store.csv',
'department_store.csv','restaurant.csv',
'cafe.csv','drugstore.csv', 'store.csv'
]

df = pd.read_csv(csv_list[0])

result = cg.coordinates(x=df["Latitude"][0], y=df["Longitude"][0])

print(result)