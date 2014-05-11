#web scraper
from sys import argv
import re
import mechanize
from BeautifulSoup import BeautifulSoup
import CSV_input
import CSV_sked_union
import dialer

#script, CSV_name = argv

csv_name = "csv_tester.csv"

#import CSV

#create CSV data struct
sked_struct = CSV_input.csv_to_dictreader(csv_name)

#for row in data strutct:
for row in sked_struct:
	#if row date is empty:
	if row['Creation_Date'] == "":
		#dial bpa with row ID
		BPA_response = dialer.return_BStable(row['Title Asset ID'],"MUSIC_CHOICE")
		####get this working at work!!

		#if ID in response
		if BPA_response:
			#pop dates from response to data struct
			CSV_sked_union.pop_date[sked_struct, BPA_response]
		#else
			#date = "not in BPA"
		row['Creation_Date'] = "not in BPA_response"
#now there should be no empty dates in DATA STRUCT

#write out DATA STRUCT to xlsx
#quit program


