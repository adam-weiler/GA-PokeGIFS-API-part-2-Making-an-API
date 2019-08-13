import requests
# import time
import dotenv
import os

# import socket

dotenv.load_dotenv()

giphy_key = os.environ.get('GIPHY_API_KEY')
query = "Pikachu"
rating = "g"

# limit = 60
# offset = 0
# total = 3551 #None?
# count = 25 #Needed?
pokemon = []

url = f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={query}&rating={rating}"


try:
    response = requests.get(url)
    # print(response.json().keys()) # Data, Pagination, Meta
    # print(response.json()['data'][0]['bitly_gif_url'])
    # print(response.json()['pagination']) # {'total_count': 3551, 'count': 25, 'offset': 0}
    # print(response.json()['meta']) # {'status': 200, 'msg': 'OK', 'response_id': '320f7798e784951f7cd60248f1e9040837a7d184'}
except:
    print('Something happened!')


if (response):
    response = response.json()
    # print(type(response['data']))

    for picture in response['data']:
        # print(picture)  # All data
        print(picture['title'])
        print(picture['bitly_gif_url'])
        print()
