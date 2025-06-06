import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Tuple
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('BookScraping')

class BookScraping():
    """Execute web screpping from base url 'https://books.toscrape.com/'."""
    def __init__(self):
        self.base_url = "https://books.toscrape.com/"
        
        try:
            logger.info('Making get request.')
            self.home_page_response = requests.get(self.base_url)
        except Exception as e:
            logger.error(f'Error to get request from {self.base_url}: {e}')
    
    def get_books_category(self):
        """Create a dict with category and categories books link"""
        cat_dict = {}
        _soup = BeautifulSoup(self.home_page_response.text, features="html.parser")
        achors = _soup.find_all('a', href=True)
        for anchor in achors:
            if 'category' in anchor.get('href'):
                cat_dict[anchor.text.strip()] = anchor.get('href')
        
        self.category_dict = cat_dict
        

    
    def request_book_category_page(self, book_category_item: Tuple) -> Dict:
        """Make a request inside of category books page an get all books in the category and
        the book link.

        Args:
            book_category_item (Tuple): A unique Dict item from the self.category_dict 

        Returns:
            Dict: A Dict of all books links and your catogry
        """
        #taking off the /book1 link
        cat, book_category_href = book_category_item
        _book_link = {}
        _response = requests.get(self.base_url+book_category_href)
        _soup = BeautifulSoup(_response.text,features="html.parser")
        articles = _soup.find_all("article", class_="product_pod")
        for i,article in enumerate(articles):
            anchor = article.find_all("a", href=True)
            _book_link[i] = {anchor[0].get('href').replace('../../../',''):cat}
            
        return _book_link
    
            
    def print_something(self):
        self.get_books_category()
        book_link_list = self.request_book_category_page(book_category_item=list(self.category_dict.items())[1])
        print(book_link_list)
        #print(self.list_categories)
        
        
    
if __name__ == '__main__':
    scrap = BookScraping()
    scrap.print_something()
    #scrap.print_something()