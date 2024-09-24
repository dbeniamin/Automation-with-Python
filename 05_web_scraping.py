# Scraping with beautiful soup

import requests
from bs4 import BeautifulSoup

# -----> Scraping one page <------

url = "https://market.feedbooks.com/category/FBHIS000000"

response = requests.get(url, headers={"Accept": "text/html"})

parsed_response = BeautifulSoup(response.text, "html.parser")

# print(parsed_response.prettify())

# extract info from the scraped data
# find elements by class_ and by "a" indicator
book_titles = parsed_response.find_all("a", class_="block__item-title")
for title in book_titles:
    print(title.text)


# -----> Scraping multiple pages <------

base_url = "https://market.feedbooks.com/top?page="
# create an empty list to save the titles from all pages
titles_test = []

# the loop goes up to page 3 of the pages
for number in range(3):
    # make a loop to adapt the url that has multiple pages
    scrape_url = f"{base_url}{number}"
    # print(scrape_url)
    response_test = requests.get(scrape_url, headers={"Accept": "text/html"})
    parsed_test = BeautifulSoup(response_test.text, "html.parser")
    book_titles = parsed_test.find_all("a", class_="block__item-title")
    # append titles in the previous empty list created
    for title in book_titles:
        titles_test.append(title.text)
        # print(f"The page number is: {number} and the book tile is: {title.text}")

print(titles_test)

