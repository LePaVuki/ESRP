import requests

BASE_URL = "https://esi.evetech.net/latest"

def getListOfSystmesId():
    # gets all the system ids
    system_ids = requests.get(f"{BASE_URL}/universe/systems/?datasource=tranquility")

    # transforms response to json
    return(system_ids.json())

def getListOfConstellationsId():
    # gets all the system ids
    constellations_ids = requests.get(f"{BASE_URL}/universe/constellations/?datasource=tranquility")

    # transforms response to json
    return(constellations_ids.json())

def getListOfRegionsId():
    # gets all the system ids
    regions_ids = requests.get(f"{BASE_URL}/universe/regions/?datasource=tranquility")

    # transforms response to json
    return(regions_ids.json())

def main():
    print(getListOfRegionsId())

if __name__ == "__main__":
    main()