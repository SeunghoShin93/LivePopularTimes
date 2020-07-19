import livepopulartimes
import pprint

result = livepopulartimes.get_populartimes_by_PlaceID("apikey","ChIJ-5cOJL-PaDURix8BdKuOMiA")

pprint.pprint(result)