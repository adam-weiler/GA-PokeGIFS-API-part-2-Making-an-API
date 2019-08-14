from django.http import JsonResponse
import dotenv
import os
import json
import random
import requests

dotenv.load_dotenv()
giphy_key = os.environ.get('GIPHY_API_KEY')


def pokemon_search(request, query):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
        body = json.loads(response.content)
        name = body['name']
        poke_id = body['id']
        types = body['types']
        
        
        try:
            response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}&rating=g')
            body = json.loads(response.content)

            random_num = random.randint(0,len(body['data']))

            gif_url = body['data'][random_num]['url']

            # breakpoint()



            return JsonResponse({ 
                'name': name,
                'poke_id': poke_id,
                'types': types,
                'gif_url': gif_url,
            })
        except:
            return JsonResponse({
                'error': response.status_code,
                'message': 'Giphy error: Something happened!'
            })
    except:
        return JsonResponse({
            'error': response.status_code,
            'message': 'Pokeapi error: Something happened!'
        })