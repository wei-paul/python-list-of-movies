import requests
from decouple import config
import pprint

api_key = config('api_key')

movie_id = 550

api_base_url = 'https://api.themoviedb.org/3'

endpoint_path = f"/movie/{movie_id}"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

r = requests.get(endpoint).json()

pprint.pprint(r)

pprint.pprint(r["production_companies"][2].get('name'))
