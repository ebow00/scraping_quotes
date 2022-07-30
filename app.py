import requests

from pages.quotes_pages import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(f'{quote.content} -- {quote.author}{quote.tag_list}')
