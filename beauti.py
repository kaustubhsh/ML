#!usr/bin/ python3
from urllib.request import urlopen
from bs4 import BeautifulSoup

url ="http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/"
html = urlopen(url)

soup = BeautifulSoup(html,'lxml')
#print(soup)

#type(soup)
'''#bs4.BeautifulSoup
#title
title = soup.title
print (title)
#<tit>
#print the text
text = soup.get_text()
print(soup.text)'''
# results in table

table=soup.find('table',attrs={'class': 'tableSorter'})
results= table.find_all('tr')
print (results)
#print('Number of results : ', len(results))
 
