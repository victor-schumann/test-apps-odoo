import requests

response = requests.get('https://randomuser.me/api/?results=2&inc=name')
data = response.json()

# Extract and print the names of the two random users
for user in data['results']:
    name = user['name']
    full_name = f"{name['first']} {name['last']}"
    print(full_name)
