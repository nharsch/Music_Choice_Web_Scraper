#from sys import argv
import csv
from CSV_input import csv_to_dictreader, dictreader_to_csv
import openpyxl

def find_asset(search_id, search_dict):
	for row in search_dict:
		if search_id == row['Asset ID'][-8:-1]:
			return row

def find_date(search_id, search_dict):
	'''search for match in search_dict, return'''
	for row in search_dict:
		if search_id == row['Asset ID'][-8:-1]:
			return row['Package Creation Date'] #grab asset id end



def pop_date(sked_dict, rs_dict):
	for row in rs_dict:
		search_id = row['Asset ID'][-8:]
		write_date = row['Package Creation Date']
		for row in sked_dict:
			if row['Title Asset ID'][-8:] == search_id:
				row['Creation_Date'] = write_date
	return sked_dict

####Get this working at work!!!!
def pop_date_BStable(sked_dict, BStable):
	for row in BStable:
		search_id = row['Asset ID'][-8:]
		write_date = row['Package Creation Date']
		for row in sked_dict:
			if row['Title Asset ID'][-8:] == search_id:
				row['Creation_Date'] = write_date
	return sked_dict

# def pop_date(sked_dict, rs_dict):
# 	'''returns list of id, date pair lists'''
# 	#result = []
# 	for row in sked_dict:
# 		if len((row['Creation_Date'])) == 0: #look for empty date values in sked_dict
# 			search_id = row['Title Asset ID'][-8:-1] #grab asset id end
# 			row['Creation_Date'] = find_date(search_id,rs_dict) #pop creation date
# 	return sked_dict

# def union_skeds_New_xlsx(sked_dict, rs_dict):
# 	married_sked = pop_date(sked_dict, rs_dict)
# 	for row in married_sked:
# 		for e in row:
			

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

	for row in sked_dict:
		print row['Creation_Date']

	print "_" * 10

	for row in pop_date(sked_dict, rs_dict):
		print row['Creation_Date']



