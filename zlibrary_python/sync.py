from bs4 import BeautifulSoup
from functools import cache
import requests

from .common import URIs, cleanup_dict

uris = URIs()

@cache
def srape_search_query(query, fuzzy = False):
    html = requests.get(uris.search_url(query)).text
    soup = BeautifulSoup(html, 'html.parser')
    if not fuzzy:
        books = soup.find_all('div', {'class': 'exactMatch'})
    else:
        books = soup.find_all('div', {'class': 'resItemBoxBooks'})
    return [process_book(book) for book in books]

def process_book(book: BeautifulSoup):
    def safe_year():
        if (found := book.find('div', {'class': 'property_year'})):
            if (year := found.find('div', {'class': 'property_value'})):
                return year.text
            
    def safe_language():
        if (found := book.find('div', {'class': 'property_language'})):
            if (language := found.find('div', {'class': 'property_value'})):
                return language.text
       
    return cleanup_dict({
        'title': (title := book.find('h3', {'itemprop': 'name'})).text,
        'url': uris.book_url(*title.find('a')['href'].split('/')[-2:]),
        'downloadurl': uris.download_url(*title.find('a')['href'].split('/')[-2:]),
        'author': book.find('a', {'itemprop': 'author'}).text,
        'publisher': book.find('a', {'title': 'Publisher'}).text,
        'year': safe_year(),
        'language': safe_language(),
        'rating': {
            'interest': book.find('span', {'class': 'book-rating-interest-score'}).text,
            'quality': book.find('span', {'class': 'book-rating-quality-score'}).text,
        }
    })