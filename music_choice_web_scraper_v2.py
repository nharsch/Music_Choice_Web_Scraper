#web scraper
from csv import DictWriter
from sys import argv
import re
import mechanize
from BeautifulSoup import BeautifulSoup
import CSV_input
import CSV_sked_union
import dialer
import openpyxl


#script, CSV_name = argv

csv_name = "csv_tester.csv"

csv_headers = CSV_input.header_to_fieldnames(csv_name)

#import CSV

#create CSV data struct
sked_struct = CSV_input.csv_to_dictreader(csv_name)

#for row in data strutct:
def dial_and_pop(sked_struct):
	for row in sked_struct:
		#if row date is empty:
		if row['Creation_Date'] == "":
			#dial bpa with row ID
			BPA_response = dialer.return_BSdict(row['Title Asset ID'],"MUSIC_CHOICE")
			####get this working at work!!
			#if ID in response
			if BPA_response:
				#pop dates from response to data struct
				CSV_sked_union.pop_date(sked_struct, BPA_response)
				return sked_struct
			row['Creation_Date'] = "not in BPA response"
			#date = "not in BPA"
#now there should be no empty dates in DATA STRUCT
dial_and_pop(sked_struct)


#write out DATA STRUCT to csv
csv_output = open('csv_output.csv', 'wb')
CSV_out_writer = DictWriter(csv_output, csv_headers, dialect='excel')
CSV_out_writer.writeheader()
for row in sked_struct:
	CSV_out_writer.writerow(row)


#write out DATA STRUCT to xlsx
#quit program


