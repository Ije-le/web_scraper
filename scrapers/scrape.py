import requests
from bs4 import BeautifulSoup

url = 'https://www.mbp.state.md.us/sanctions.aspx'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
html = response.content

soup = BeautifulSoup(html, features = 'html.parser')
table = soup.find('tbody')

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        text = ' '.join(cell.text.split())
        list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    print(list_of_rows)