from csv import DictWriter
from csv import reader
from sys import argv
import re
import mechanize
from BeautifulSoup import BeautifulSoup
import CSV_input
import CSV_sked_union
import dialer
import openpyxl


script, csv_name = argv

# test_row = reader((open(csv_name)))
# row_1 = test_row.next()
# row_2 = test_row.next()
# print row_1
# print row_2

csv_headers = CSV_input.header_to_fieldnames(csv_name)


#import CSV

#create CSV data struct
sked_struct = CSV_input.csv_to_dictreader(csv_name, csv_headers)


#for row in data strutct:
def dial_and_pop(sked_struct):
	for row in sked_struct:
		#if row date is empty
		if row['Creation_Date'] == "":
			#dial bpa with row ID
			BPA_response = dialer.return_BSdict(row['Title Asset ID'], row['Provider'])
			####get this working at work!!
			#if ID in response
			if BPA_response:
				#pop dates from response to data struct
				CSV_sked_union.pop_date(sked_struct, BPA_response)
			else:
				row['Creation_Date'] = "not in BPA response"	
	return sked_struct
	
			#date = "not in BPA"
#now there should be no empty dates in DATA STRUCT
dial_and_pop(sked_struct)

#fix provider bug
for row in sked_struct:
	row['Provider'] = "MUSIC_CHOICE"

#write out DATA STRUCT to csv
csv_output = open(csv_name[:-4]+"_BPA_output.csv", 'wb')
CSV_out_writer = DictWriter(csv_output, csv_headers, dialect = 'excel')
#CSV_out_writer.writeheader()
for row in sked_struct:
	CSV_out_writer.writerow(row)

print "It worked."

# wb = openpyxl.Workbook()
# dest_filename = csv_name[:-4]
# ws = wb.active
# ws.title = csv_name[:-4]

# wb.save(filename = dest_filename+".xlsx")





#write out DATA STRUCT to xlsx
#quit program


