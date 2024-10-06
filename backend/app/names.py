import requests
import json

BASE_URL = "https://esi.evetech.net/latest"

ids_list = [34000182, 34000140, 34000101]
json_ids = json.dumps(ids_list)
# gets all the system ids
response = requests.post(f"{BASE_URL}/universe/names/?datasource=tranquility")
json_names = json.loads(response.content)
print(json_names['ids'])