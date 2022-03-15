import requests
from decouple import config
import pprint

api_key = config('api_key')

movie_id = 500

api_base_url = 'https://api.themoviedb.org/3'

endpoint_path = f"/movie/top_rated"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&language=en-US&page=1"

r = requests.get(endpoint).json()

results = r['results']

if len(results) > 0:
    for result in results:
        print(result['title'])
