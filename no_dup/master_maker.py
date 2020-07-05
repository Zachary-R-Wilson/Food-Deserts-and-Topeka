import pandas as pd
csv_list=['bakery.csv','home_goods_store.csv','supermarket.csv',
'convenience_store.csv','liquor_store.csv',
'department_store.csv','restaurant.csv',
'cafe.csv','drugstore.csv', 'store.csv'
]
names = []
addresses = []
lats = []
lngs = []
master_df = pd.DataFrame({
    "Name": names,
    "Address": addresses,
    "Latitude": lats,
    "Longitude": lngs,
})
for i in range(10):
    df = pd.read_csv(csv_list[i])
    df.drop(inplace = True,columns="Unnamed: 0")
    master_df = master_df.append(df,ignore_index=True)

master_df.drop_duplicates(inplace = True, ignore_index=True)
master_df.to_csv("../Resources/master.csv")