from django.http import HttpResponse,JsonResponse
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from .models import Show, Movie
# # from .permissions import IsOwnerOrReadOnly
# from .serializers import ShowSerializer, MovieSerializer

def get_genres(request):
    url = 'https://partner-api.reelgood.com/v1.0/meta/genres'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        data2 = {"genres": trim_genres(data)}
        return JsonResponse(data2, safe=False)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

def trim_genres(data):
    genres_to_keep = ['Action', 'Documentary', 'Fantasy', 'Musical', 'Romance', 'Peacock', 'Science-Fiction', 'Comedy', 'Drama', 'Horror', 'Children', 'Family', 'Mystery', 'Western', 'Animation', 'Anime']
    trimmed_data = [d for d in data if d["name"] in genres_to_keep]
    return trimmed_data

#Have to figure out where/how we are getting the search request from the frontend
def search(request):
    term=request.GET.get('term', '')
    url = f'https://partner-api.reelgood.com/v1.0/content/search?term={term}&all_services=true&content_type=Both'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

def get_services(request):
    url = 'https://partner-api.reelgood.com/v1.0/meta/services'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        data2 = {"services": trim_services(data)}
        return JsonResponse(data2, safe=False)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

def trim_services(data):
    services_to_keep = ['Netflix', 'Hulu', 'Prime Video', 'HBO Max', 'Crunchyroll', 'Peacock', 'Paramount+', 'Disney+']
    trimmed_data = [d for d in data if any(service["display_name"] in services_to_keep for service in d["services"])]
    return trimmed_data

#Have to figure where/how we are pulling service ids
def get_popular_based_on_service(request):
    service_ids = [1, 2, 4]  # Example list of service ids
    service_ids_str = ''.join(f'&service={id}' for id in service_ids)
    url = f'https://partner-api.reelgood.com/v1.0/content/browse/Both?order_by=Popular&all_services=false{service_ids_str}'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

# Netflix id = 1
# Prime id = 2
# Hulu id = 4
# crunchyroll id = 12
# Prime(free) id = 78
# crunchyroll(free) id = 92
# Hulu(free)  id = 115
# Disney+ id = 353 
# Peacock(free) = 367
# Paramount+ = 375
