import requests
import json


def main():
    BASE_URL = "https://esi.evetech.net/latest"

    # gets all the system ids
    system_ids = requests.get(f"{BASE_URL}/universe/systems/?datasource=tranquility")

    # transforms all ids to text
    datastr = system_ids.text

    print(datastr)


if __name__ == "__main__":
    main()
