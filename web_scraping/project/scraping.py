import requests
from bs4 import BeautifulSoup
from csv import writer,DictWriter
from random import choice
import io
#from time import sleep

base_url = "https://quotes.toscrape.com"
url = "https://quotes.toscrape.com/page/{}/"

def scrape_quotes():
	all_quotes = []
	page = 1
	page_still_valid = True
	while page_still_valid:
		page_url = url.format(page)
		response = requests.get(page_url)

		if "No quotes found!" in response.text:
			break

		soup = BeautifulSoup(response.text, "html.parser")
		quotes = soup.select(".quote")
		for quote in quotes:
			all_quotes.append({
				"text":quote.find(class_="text").text,
				"author":quote.find(class_="author").text,
				"bio-link":quote.find("a")["href"]
				})
		page +=1
		# sleep(2)
	print(len(all_quotes))
	return all_quotes

def write_quotes(quotes):
	with io.open("quotes.csv", "w", newline="", encoding="utf-8") as file:
		headers = ["text","author","bio-link"]
		csv_writer = DictWriter(file, fieldnames=headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)