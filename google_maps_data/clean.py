import pandas as pd
csv_list=['bakery.csv','home_goods_store.csv','supermarket.csv',
'bank.csv','convenience_store.csv','liquor_store.csv',
'bar.csv','department_store.csv','restaurant.csv',
'cafe.csv','drugstore.csv', 'store.csv'
]
for i in range(12):
    df = pd.read_csv(csv_list[i])
    df.drop(inplace = True,columns="Unnamed: 0")
    df.drop_duplicates(inplace = True, ignore_index=True)
    df.to_csv("../no_dup/" + csv_list[i])