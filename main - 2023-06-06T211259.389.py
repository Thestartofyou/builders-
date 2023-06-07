import requests

def search_builders(location):
    url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json&addressdetails=1"
    response = requests.get(url)
    data = response.json()

    builders = []

    for item in data:
        if 'builder' in item['address']:
            builders.append(item['address']['builder'])

    return builders

# Example usage
location = "New York"
builders = search_builders(location)

if builders:
    print(f"Builders in {location}:")
    for builder in builders:
        print(builder)
else:
    print("No builders found in the specified location.")
