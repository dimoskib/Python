import requests

url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":"cat","limit":1})

data = response.json()

one_joke = data["results"]
joke = one_joke[0]
#print(data["results"])
#print(data["joke"])
print(joke["joke"])
