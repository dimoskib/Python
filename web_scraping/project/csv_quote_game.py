import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice

def read_quotes(filename):
	with open(filename, "r") as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

def start_game(quotes):
	quote = choice(quotes)
	remaining_quesses = 4
	print("Here's a quote: ")
	print(quote["text"])
	print(quote["author"])
	quess = ""
	while quess.lower() != quote["author"].lower() and remaining_quesses>0:
		quess = input(f"Who said this quote? Guesses remaining: {remaining_quesses}  ")
		if quess.lower() == quote["author"].lower():
			print("You got it right.")
			break
		remaining_quesses -= 1
		if remaining_quesses == 3:
			response = requests.get(f"{base_url}{quote['bio-link']}")
			soup = BeautifulSoup(response.text,"html.parser")
			birth_date = soup.find(class_="author-born-date").text
			birth_place = soup.find(class_="author-born-location").text
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
		elif remaining_quesses == 2:
			print(f"Here's a hint: The author's first name starts with {quote['author'][0]}")
		elif remaining_quesses == 1:
			last_initial = quote['author'].split(' ')[1][0]
			print(f"Here's a hint: The author's last name starts with {last_initial}")
		else:
			print(f"Sorry, you ran out of guesses. The answer was {quote['author']}")

	again = ''
	while again not in ('y','yes','n','no'):
		again = input("Would you like to play again (y/n)? ")
	if again.lower() in ('yes','y'):
		return start_game(quotes)
	else:
		print("Okay, goodbye!")

quotes = read_quotes("data.csv")
start_game(quotes)
