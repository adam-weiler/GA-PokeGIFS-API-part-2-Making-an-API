from django.http import JsonResponse
import json
import requests


def pokemon_search(request, search_query):
  
    result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{search_query}')
    body = json.loads(result.content)
    
    return JsonResponse({ 
        'name': body["name"],
        'id': body["id"],
        'types': body["types"],
    })