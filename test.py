import livepopulartimes
import pprint
from decouple import config

SECRET_KEY = config('API_KEY')

# result = livepopulartimes.get_populartimes_by_PlaceID(SECRET_KEY,"ChIJ-5cOJL-PaDURix8BdKuOMiA")

result = livepopulartimes.get_places_by_search("Shinsung-dong")
pprint.pprint(result)

# num = 0
# for place in result:
#     num += 1
#     print(str(num) + '.', end = ' ')
#     print(place['name'])
#     print(place['place_id'])
#     print('----------')