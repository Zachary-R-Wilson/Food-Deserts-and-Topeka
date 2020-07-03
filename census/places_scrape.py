#Dependencies
import requests, json
import pandas as pd
import time
#Google developer API key
#from ba_config import g_key
from zw_config import g_key

#constants
target_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

query = ["food bank", "food pantry", "bakery", "grocery store", "restaurant", "dollar general", 
         "family dollar", "dollar tree", "department store"]

types = ["bakery","bank","bar","cafe","convenience_store","department_store",
         "drugstore","home_goods_store","liquor_store","restaurant","store","supermarket"]

#create the master dataframe
names = []
addresses = []
lats = []
lngs = []

dmaster = pd.DataFrame({
    "Name": names,
    "Address": addresses,
    "Latitude": lats,
    "Longitude": lngs,
})

#create for loop to loop through all the types
i = 0
for i in range(12):
    #start and end points
    ori_lat = 39.108452
    ori_lon = -95.816615
    end_lat = 38.913316
    end_lon = -95.594971

    #create the main dataframe
    names = []
    addresses = []
    lats = []
    lngs = []

    dfull = pd.DataFrame({
        "Name": names,
        "Address": addresses,
        "Latitude": lats,
        "Longitude": lngs,
    })

    var_lat = ori_lat
    while ori_lon < end_lon:
        #create params
        params = {
            "location":str(var_lat) + "," + str(ori_lon),
            "radius":805,
            "type": types[i],
            "key": g_key
        }
        #generate & send request
        response = requests.get(target_url, params)
        food_response = response.json()
        #empty old lists
        names = []
        addresses = []
        lats = []
        lngs = []
        #create filler dataframe
        for food_response in food_response["results"]:
            names.append(food_response["name"])
            addresses.append(food_response["vicinity"])
            lats.append(food_response["geometry"]["location"]["lat"])
            lngs.append(food_response["geometry"]["location"]["lng"])
        #complete df
        df = pd.DataFrame({
            "Name": names,
            "Address": addresses,
            "Latitude": lats,
            "Longitude": lngs
        }) 
        #push to main dataframe
        dfull = dfull.append(df, ignore_index=True)
        #pause for a second so google doesn't charge me
        time.sleep(1)
        #increase the var_lat
        var_lat -= .01
        if var_lat <= 38.91:
            ori_lon += .01
            var_lat = ori_lat
            print("PROCESSING")

    dfull.to_csv(str(types[i])+".csv")
    dmaster = dmaster.append(dfull, ignore_index=True)
dmaster.to_csv("master.csv")