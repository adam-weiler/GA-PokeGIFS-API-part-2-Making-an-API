from django.http import JsonResponse
import dotenv
import os
import json
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
            gif_url = body['data'][0]['url']





            return JsonResponse({ 
                'name': name,
                'poke_id': poke_id,
                'types': types,
                'gif_url': gif_url,
            })
        except:
            return JsonResponse({
                'message': 'Something happened!'
            })
    except:
        return JsonResponse({
            'message': 'Something happened!'
        })