import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.mbp.state.md.us/sanctions.aspx'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')
print(soup.prettify())

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        text = ' '.join(cell.text.split())
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["url", "name", "type", "date"])
writer.writerows(list_of_rows)

