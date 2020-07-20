import livepopulartimes
import pprint
from decouple import config

SECRET_KEY = config('API_KEY')

result = livepopulartimes.get_populartimes_by_PlaceID(SECRET_KEY,"ChIJ-5cOJL-PaDURix8BdKuOMiA")

pprint.pprint(result)