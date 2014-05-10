#from sys import argv
import csv
from CSV_input import csv_to_dictreader
import openpyxl

def find_date(search_id, rs_dict):
	'''search for mach in rs_dict, return'''
	for row in rs_dict:
		if search_id == row['Asset ID'][-8:-1]:
			return row['Package Creation Date'] #grab asset id end


def pop_date(sked_dict, rs_dict):
	'''returns list of id, date pair lists'''
	#result = []
	for row in sked_dict:
		if len((row['Creation_Date'])) == 0: #look for empty date values in sked_dict
			search_id = row['Title Asset ID'][-8:-1] #grab asset id end
			row['Creation_Date'] = find_date(search_id,rs_dict) #pop creation date
	return sked_dict

def union_skeds_New_xlsx(sked_dict, rs_dict):
	married_sked = pop_date(sked_dict, rs_dict)
	for row in married_sked:
		for e in row:
			

# def dict_list_to_csv(dict_list):
# 	'''take custom dict list, returns nice csv'''
# 	return csv

# def response_table_to_dictreader(table):

########################
if __name__ == '__main__':
	sked = "csv_tester.csv"
	online_response = "csv_online_tester.csv"

	sked_dict = csv_to_dictreader(sked)
	rs_dict = csv_to_dictreader(online_response)

	print sked_dict
	print pop_date(sked_dict, rs_dict)



