import requests
import json


def main():
    BASE_URL = "https://esi.evetech.net/latest"

    ROUTE_ORIGIN = "30000142"  # Jita
    ROUTE_DESTINATION = "30000165"  # Ishisomo

    # Build a route between ROUTE_ORIGIN and ROUTE_DESTINATION
    # Get route data based on a list of ids
    route_ids = requests.get(
        f"{BASE_URL}/route/{ROUTE_ORIGIN}/{ROUTE_DESTINATION}/?datasource=tranquility"
    )

    # Route data is in str
    route_data_str = requests.post(f"{BASE_URL}/universe/names", route_ids).text

    # Transform raw str to JSON object
    route_data = json.loads(route_data_str)
    # Select only names of route systems in JSON object
    route_names = [x["name"] for x in route_data]

    print(route_names)


if __name__ == "__main__":
    main()
