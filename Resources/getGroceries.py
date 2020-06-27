
import requests
import json
import csv

gkey = "AIzaSyDZ0NStSeomJLtlfN4UE3YMfDXWlBpi8A0"
# 39.0473° N, 95.6752° W
# 39.0375° N, 95.7680°
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
#drugstore , gas_station,pharmacy
params = {
    "location": "39.0375,-95.7680",  # philadelphia coords,
    # "rankby": "distance",
    "type": "gas",
    "key": gkey,
    "radius": "50000"
}

stores = []

response = requests.get(base_url, params=params).json()

# extract results
results = response['results']

for r in results:
    stores.append(r)


params['page_token'] = response['next_page_token']
response = requests.get(base_url, params=params).json()
# extract results
results = response['results']

for r in results:
    stores.append(r)

params['page_token'] = response['next_page_token']
response = requests.get(base_url, params=params).json()
# extract results
results = response['results']

for r in results:
    stores.append(r)

token = response['next_page_token']


print(stores.__len__())
csv_columns = ['name', 'opening_hours', 'price_level', 'id', 'scope', 'rating', 'types', 'plus_code',
               'user_ratings_total', 'vicinity', 'place_id', 'business_status', 'geometry', 'photos', 'reference', 'icon']

try:
    with open("gas.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in stores:
            writer.writerow(data)
except IOError:
    print("I/O error")

# with open("stores.csv", 'wb') as csv_file:
#     wr = csv.writer(csv_file, delimiter=',')
#     for r in results:
#         wr.writerow(list(r))
# 'business_status': 'OPERATIONAL',
# 'geometry': {'location': {'lat': 39.0474948, 'lng': -95.6748535},
#  'viewport': {'northeast': {'lat': 39.0488715802915, 'lng': -95.67361296970849},
#  'southwest': {'lat': 39.0461736197085, 'lng': -95.67631093029149}}},
#  'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/bank_dollar-71.png',
#  'id': '7b7c5fde3a726cb8251b0d5d7cfd7a367e049656',
#  'name': 'CoreFirst Bank & Trust', 'opening_hours':
#   {'open_now': False}, 'place_id': 'ChIJnaV91BEDv4cRf5ahc2WC5M8',
#    'plus_code': {'compound_code': '28WG+X3 Topeka, KS, United States', 'global_code': '86F628WG+X3'},
#    'rating': 2, 'reference': 'ChIJnaV91BEDv4cRf5ahc2WC5M8', 'scope': 'GOOGLE',
#    'types': ['bank', 'atm', 'finance', 'point_of_interest', 'establishment'],
#    'user_ratings_total': 4, 'vicinity': '830 South Kansas Avenue, Topeka'}
