from django.http import HttpResponse,JsonResponse
from dotenv import load_dotenv
import os
import requests
import json
load_dotenv()

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

def search(request):
    term='Titanic'
    url = f'https://partner-api.reelgood.com/v1.0/content/search?term={term}&all_services=true&content_type=Both'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return HttpResponse(response)
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
        # data2 = trim_services(data)
        return JsonResponse(data2, safe=False)
        # return HttpResponse(response)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

def trim_services(data):
    services_to_keep = ['Netflix', 'Hulu', 'Prime Video', 'HBO Max', 'Crunchyroll', 'Peacock', 'Paramount+', 'Disney+']
    trimmed_data = [d for d in data if any(service["display_name"] in services_to_keep for service in d["services"])]
    return trimmed_data

    
    

# class ShowList(ListCreateAPIView):
#     queryset = Show.objects.all()
#     serializer_class = ShowSerializer


# class ShowDetail(RetrieveUpdateDestroyAPIView):
#     # permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Show.objects.all()
#     serializer_class = ShowSerializer

# class MovieList(ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# class MovieDetail(RetrieveUpdateDestroyAPIView):
#     # permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
