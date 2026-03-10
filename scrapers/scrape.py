import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup

CSV_PATH = os.path.join(os.path.dirname(__file__), "alerts.csv")
current_year = datetime.date.today().year

# Determine URL for the current year
if current_year == 2026:
    url = 'https://www.mbp.state.md.us/sanctions.aspx'
else:
    url = f'https://www.mbp.state.md.us/sanctions_{current_year}.aspx'

print(f"Scraping {url}")
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.114 Safari/537.36'
})
response.raise_for_status()

soup = BeautifulSoup(response.content, features="html.parser")
table = soup.find('tbody')

new_rows = []
for row in table.find_all('tr'):
    cells = [current_year]
    for cell in row.find_all('td'):
        if cell.find('a'):
            href = cell.find('a')['href']
            if href.startswith('http'):
                cells.append(href)
            else:
                cells.append('https://www.mbp.state.md.us' + href)
        else:
            cells.append(' '.join(cell.text.split()))
    new_rows.append(cells)

# Read existing CSV, keeping all rows that are NOT from the current year
existing_rows = []
if os.path.exists(CSV_PATH):
    with open(CSV_PATH, newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if row and str(row[0]) != str(current_year):
                existing_rows.append(row)

# Write header + historical rows + fresh current-year rows
with open(CSV_PATH, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["url", "name", "type", "date"])
    writer.writerows(existing_rows)
    writer.writerows(new_rows)

print(f"Done. {len(new_rows)} rows written for {current_year}.")