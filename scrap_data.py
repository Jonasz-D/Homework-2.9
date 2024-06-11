import requests, json
from bs4 import BeautifulSoup

def run_beautiful_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def scrap_quotes(url):
    soup = run_beautiful_soup(url)
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    list_of_quotes = []
    for num in range(0, len(quotes)):
        quote = {}

        quote['quote'] = quotes[num].text
        quote['author'] = authors[num].text

        list_of_tags = []
        quote['tags'] = list_of_tags
        tags_for_quote = tags[num].find_all('a', class_='tag')
        for tag in tags_for_quote:
            list_of_tags.append(tag.text)
      
        list_of_quotes.append(quote)
    return list_of_quotes

def inner_url(url):
    soup = run_beautiful_soup(url)
    links = soup.find_all('a')
    list_of_links = []
    for link in links:
        link = link['href']
        if link.startswith('/author/'):
            link = f'{url}{link}/'
            list_of_links.append(link)
    return list_of_links

def scrap_authors_by_url(soup:BeautifulSoup):
    author = {}
    fullname = soup.find('h3', class_='author-title')
    fullname = fullname.get_text()
    author['fullname'] = fullname

    born_date = soup.find('span', class_='author-born-date')
    born_date = born_date.get_text()
    author['born_date'] = born_date

    born_location = soup.find('span', class_='author-born-location')
    born_location = born_location.get_text()
    author['born_location'] = born_location

    author_description = soup.find('div', class_='author-description')
    author_description = author_description.get_text().strip()
    author['description'] = author_description

    return author

def scrap_authors(url):
    inner_urls = inner_url(url)
    list_of_authors = []
    for url in inner_urls:
        soup = run_beautiful_soup(url)
        list_of_authors.append(scrap_authors_by_url(soup))
    return list_of_authors