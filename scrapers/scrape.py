import csv
import datetime
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.mbp.state.md.us/sanctions.aspx'
all_rows = []

# Loop through years from 2010 to 2026
for year in range(2017, 2027):
    print(f"Scraping {year}...")
    if year == 2020:
        continue
    if year < datetime.date.today().year:
        url = f'https://www.mbp.state.md.us/sanctions_{year}.aspx'
    else:
        url = base_url
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('tbody')

    for row in table.find_all('tr'):
        # Skip wrapper rows that contain <tr> elements but no direct <td> children
        if not row.find_all('td', recursive=False):
            continue
        list_of_cells = [str(year)]
        for cell in row.find_all('td'):
            if cell.find('a'):
                href = cell.find('a')['href']
                if href.startswith('http'):
                    list_of_cells.append(href)
                else:
                    list_of_cells.append("https://www.mbp.state.md.us" + href)
                if year < 2026:
                    list_of_cells.append(cell.find('a').text.strip())
            else:
                text = ' '.join(cell.text.split())
                list_of_cells.append(text)
        all_rows.append(list_of_cells)

outfile = open("all_sanctions.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["year", "url", "name", "type", "date"])
writer.writerows(all_rows)
print(f"Scraped {len(all_rows)} total records!")