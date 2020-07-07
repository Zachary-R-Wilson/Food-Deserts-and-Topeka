import pandas as pd
csv_list=['bakery.csv','home_goods_store.csv','supermarket.csv',
'convenience_store.csv','liquor_store.csv',
'department_store.csv','restaurant.csv',
'cafe.csv','drugstore.csv', 'store.csv'
]
table_list=['bakery','home_goods_store','supermarket',
'convenience_store','liquor_store',
'department_store','restaurant',
'cafe','drugstore', 'store'
]
names = []
addresses = []
lats = []
lngs = []
csv_name = []
master_df = pd.DataFrame({
    "Name": names,
    "Address": addresses,
    "Latitude": lats,
    "Longitude": lngs,
    "Table Name":csv_name
})
for i in range(10):
    df = pd.read_csv(csv_list[i])
    df.drop(inplace = True,columns="Unnamed: 0")
    df["Table Name"] = table_list[i]
    master_df = master_df.append(df,ignore_index=True)

master_df.drop_duplicates(inplace = True, ignore_index=True)
master_df.to_csv("../Resources/master.csv")