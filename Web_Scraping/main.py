import requests
import re
from bs4 import BeautifulSoup


url = "http://localhost:3333/"

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
top_heading = parsed_html.select_one('body')
if top_heading is not None:
    titulo = top_heading.parent
    if titulo is not None:
        for p in titulo.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip(''))
print(response.status_code)

# print(response.headers)
# print(response.content)
print(parsed_html.title.text)