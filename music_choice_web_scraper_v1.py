#web scraper
from sys import argv
import re
import mechanize
from BeautifulSoup import BeautifulSoup

script, assetID = argv

assetID = assetID[:-1]

br = mechanize.Browser()
br.open("http://bpa2.indemand.com/package-search/")

bs = BeautifulSoup

#here's the submit form
'''
csrfmiddlewaretoken:973cb199cb58e4c66f442b70843295bb
assetName:
title:
assetID:
rowCreationTime:
dateDirection:gte
studioName:
provider:MUSIC_CHOICE
licStartDate:
licStartDateDirection:gte
licEndDate:
licEndDateDirection:gte
processingID:Any
'''

br.select_form(nr=0)

br.set_handle_robots(False)

br['assetID'] = assetID
br['provider'] = "MUSIC_CHOICE"

postdict = {'assetID' : assetID,
			'provider' : 'MUSIC_CHOICE'
			}


#submit
rs = br.submit()
html = rs.read()
soup = BeautifulSoup(html)
table = soup.find("table")

response = ""


#search table and populate columms
for row in table.findAll('tr')[1:]:
    col = row.findAll('td')
    date = col[0].string
    asset_name = col[1].string
    response += date+"\t"

print response
print "it works"