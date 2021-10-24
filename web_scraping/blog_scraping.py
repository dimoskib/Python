# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog?page={}"


with open("blog_data.csv","a",newline='') as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(["title","link","date"])

for n in range(1,8):
	scrape_url = url.format(n)
	response = requests.get(scrape_url)
	soup = BeautifulSoup(response.text, "html.parser")
	articles = soup.find_all("article")

	with open("blog_data.csv","a",newline='') as csv_file:
		csv_writer = writer(csv_file)
		for article in articles:
			a_tag = article.find("a")
			title = a_tag.text
			href = a_tag["href"]
			date = article.find("small").text
			csv_writer.writerow([title, href, date])