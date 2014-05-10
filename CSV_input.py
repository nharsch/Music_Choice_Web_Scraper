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
	csvfile = open(csv_name, 'rb') #opens file
	dict_reader = []
	#make sked dict friendlier to write on
	for row in csv.DictReader(csvfile):
		dict_reader.append(row)

	return dict_reader

def	dictread_print(csv):
	dict_reader = csv_to_dictreader(csv)
 	for i in dict_reader:
 		print i


#############################
if __name__ == "__main__":
	sked = "csv_tester.csv"
	online_response = "csv_online_tester.csv"

	dictread_print(sked)
	dictread_print(online_response)