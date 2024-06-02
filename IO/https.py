import requests


url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
