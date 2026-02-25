import csv
import sys
import datetime
import requests
from bs4 import BeautifulSoup

#Get year from command line argument, or use current year if not provided.
# if len(sys.argv) > 1:
#     year = sys.argv[1]
# else:
#     year = str(datetime.now().year)

# if year == '2026':
#     url = 'https://www.mbp.state.md.us/sanctions.aspx'
# else:

outfile = open("alerts.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["url", "name", "type", "date"])

for year in range(2017,2027):
    if year == 2026:
        url = 'https://www.mbp.state.md.us/sanctions.aspx'
    else:
        url = f'https://www.mbp.state.md.us/sanctions_{year}.aspx'
    # Make a POST request to the URL with the year as a parameter
    print(url)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('tbody')

    list_of_rows = []
    for row in table.find_all('tr'):
        list_of_cells = []
        list_of_cells.append(year) #Add year as first column in csv file
        for cell in row.find_all('td'):
            if cell.find('a'):
                href = cell.find('a')['href']
                if href.startswith('http'):
                    list_of_cells.append(href)
                else:
                    list_of_cells.append('https://www.mbp.state.md.us' + href)
                #list_of_cells.append(cell.find('a')['href'])
            else:
                text = ' '.join(cell.text.split())
                list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

        writer.writerows(list_of_rows)



#I ran it with 2025 (and other years), it had 2025 as the first column but returned the same results as 2026.