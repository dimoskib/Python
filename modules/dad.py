import requests
from random import choice
import pyfiglet
from termcolor import colored
import colorama
colorama.init()

header = pyfiglet.figlet_format("DAD JOKES")
header = colored(header,color='magenta')
print(header)

url = "https://icanhazdadjoke.com/search"

users_term = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":users_term}
	)

data = response.json()
num_jokes = data["total_jokes"]
if num_jokes > 1:
	print(f"I've got {data['total_jokes']} jokes about {users_term}. Here is one: ")
	joke = data["results"][0]
	print(joke["joke"])
else:
	print(f"Sorry I don't have any jokes about {users_term}! Please try again.")
