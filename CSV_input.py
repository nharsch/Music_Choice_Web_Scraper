import csv
#from sys import argv
import os

# test_name = "csv_online_tester.csv"
#script, csv = argv

#def csv_string_to_real_csv(csv_string):
	

def csv_to_dictreader(csv_name):
	'''
	takes file path
	returns dictreader object
	'''
# script_dir = os.path.dirname(__file__) 
# print script_dir
# rel_path = "csv_tester.csv"
# abs_file_path = os.path.join(script_dir, rel_path)
# print abs_file_path

	csvfile = open(csv_name, 'rb') #opens file
#	reader = csv.reader(csvfile)
	dict_reader = csv.DictReader(csvfile)

	return dict_reader

# def dict_list_to_csv(dict_list):
# 	'''take custom dict list, returns nice csv'''
# 	return csv

# def response_table_to_dictreader(table):


if __name__ == "__main__":
	dict_reader = csv_to_dictreader("csv_tester.csv")
 	for i in dict_reader:
 		print i
	
# for i in reader:
# 	print i

# for i in dict_reader:
# 	print i['Package Creation Date'], i['Asset Name'], i['Asset ID']
# 	print i['Title Asset ID'], i['Asset Name']

# raw_input()
# print main(test_name)