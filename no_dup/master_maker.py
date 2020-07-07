import pandas as pd
import censusgeocode as cg
import time

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
tract = []
master_df = pd.DataFrame({
    "Name": names,
    "Address": addresses,
    "Latitude": lats,
    "Longitude": lngs,
    "Table Name":csv_name,
    "Tract": tract
})
for i in range(10):
    df = pd.read_csv(csv_list[i])
    df.drop(inplace = True,columns="Unnamed: 0")
    df["Table Name"] = table_list[i]
    
    result_list = []
    for j in range(df.shape[0]):
        try:
            result = cg.coordinates(x=df["Longitude"][j], y=df["Latitude"][j])
            spl_re = result['Census Tracts'][0]['NAME']
            spl_re = spl_re.split(' ')
            result_list.append(spl_re[2])
        except:
            result_list.append("")
        time.sleep(2)
    df["Tract"] = result_list
    master_df = master_df.append(df,ignore_index=True)

master_df.drop_duplicates(inplace = True, ignore_index=True)
master_df.to_csv("../Resources/master.csv")