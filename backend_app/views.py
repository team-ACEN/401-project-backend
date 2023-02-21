from django.http import HttpResponse,JsonResponse
import re
import requests
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Movie, Show
from .serializers import MovieSerializer, ShowSerializer

# url = ''

# def get_streaming_services(request):
#     text = "\n\nWall-E is available to stream on Disney+, Amazon Prime Video, iTunes, Google Play, YouTube, and Vudu."
#     regex = r'(\w[\w\s]*)(?=,|\.)\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'
#     matches = re.findall(regex, text)
#     return JsonResponse(matches, safe=False)

# def get_streaming_services_from_openai(request):
#     prompt = "Where can I stream Wall-E?"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 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"
#     }
#     data = {
#         "model": "text-davinci-003",
#         "prompt": prompt,
#         "max_tokens": 50,
#         "temperature": 0
#     }
#     response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
#     if response.status_code == 200:
#         choices = response.json()["choices"]
#         if choices and len(choices) > 0:
#             text = choices[0]["text"]
#             streaming_services = extract_streaming_services(text)
            
#             return JsonResponse(streaming_services, safe=False)
#     return JsonResponse({"error": "Failed to retrieve streaming services from OpenAI API."})

# def extract_streaming_services(text):
#   regex = r'(\w[\w\s]*)(?=,|\.)\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'
#   matches = re.findall(regex, text)
#   return matches

def get_genres(request):
    url = 'https://partner-api.reelgood.com/v1.0/meta/genres'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': 'WV107IL7Jw8KLsQJthBjlkntU9ZEVoP96ttBehhr0YTvXfOzUiOlzdETDdsoYs1dNrS5COtxfmTR4T56LkREtM6vv'
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return HttpResponse(response)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})

def search(request):
    term='Titanic'
    url = f'https://partner-api.reelgood.com/v1.0/content/search?term={term}&all_services=true&content_type=Both'
    headers = {
        'Accept': 'text/plain',
        'x-api-key': 'WV107IL7Jw8KLsQJthBjlkntU9ZEVoP96ttBehhr0YTvXfOzUiOlzdETDdsoYs1dNrS5COtxfmTR4T56LkREtM6vv'
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return HttpResponse(response)
    return JsonResponse({"error": f"Failed to retrieve genres from Reelgood API due to {response.status_code}"})


class ShowList(ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
