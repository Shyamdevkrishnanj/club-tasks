# import requests
# import csv
# from bs4 import BeautifulSoup


# url = 'https://www.worldometers.info/coronavirus/#countries'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# table = soup.find('table', {'id': 'main_table_countries_today'})

# rows = table.tbody.find_all('tr')

# data = []

# csvFile = open('Test.csv', 'wt+')
# writer = csv.writer(csvFile)

# for row in rows:
#     cols = row.find_all('td')
#     if len(cols) > 1 and not cols[0].text.strip().startswith(('World','North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania')):
#         country = cols[1].text.strip()
#         cases = cols[2].text.strip().replace(',', '')
#         deaths = cols[4].text.strip().replace(',', '')
#         recoveries = cols[6].text.strip().replace(',', '')
#         data.append([country, cases, deaths, recoveries])
#         writer.writerow(data)

# print('Top 10 countries with the most COVID-19 cases:--')
# k=0


# # print("No.   -country   no. of cases  -no of deaths  -no of recoveries")
# # for i in range(18):
       
# #        if (i>=8):
 
# #          print(f'{k+1}. {data[i][0]} - {data[i][1]} , {data[i][2]} , {data[i][3]} ')
# #          file.write(f'{k+1}. ;{data[i][0]} ;{data[i][1]} ; {data[i][2]} ; {data[i][3]} \n')
# #          k=k+1

import csv
import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.worldometers.info/coronavirus/'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table that contains the country data
table = soup.find('table', {'id': 'main_table_countries_today'})

# Find the rows of the table (excluding the header row)
rows = table.find_all('tr')[1:]

# Create a list to store the data for the top 10 countries
data = []

# Loop through the rows and extract the data for each country
for row in rows[:10]:
    # Extract the columns of the row
    columns = row.find_all('td')

    # Extract the name, total cases, total deaths, and total recovered for the country
    name = columns[1].text.strip()
    cases = int(columns[2].text.strip().replace(',', ''))
    deaths = int(columns[4].text.strip().replace(',', ''))
    recovered = int(columns[6].text.strip().replace(',', ''))

    # Add the data for the country to the list
    data.append([name, cases, deaths, recovered])

# Create a CSV file and write the data to it
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'Total Cases', 'Total Deaths', 'Total Recovered'])
    writer.writerows(data)
