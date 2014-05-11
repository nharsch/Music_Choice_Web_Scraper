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

def	dictread_print(csv_name):
	dict_reader = csv_to_dictreader(csv)
 	for i in dict_reader:
 		print i



def header_to_fieldnames(csv_name):
	header_list = []
	with open(csv_name, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for i in reader.next():
			header_list.append(i)
		return header_list


def dictreader_to_csv(dict_reader, fieldnames, csv_output):
	with open(csv_output, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames, delimiter = ',')
		writer.writeheader()
		for row in dict_reader:
			writer.writerow(row)




#############################
if __name__ == "__main__":
	sked = "csv_tester.csv"
	online_response = "csv_online_tester.csv"

	print header_to_fieldnames(sked)

	# dictread_print(sked)
	# dictread_print(online_response)

	dictreader_to_csv(csv_to_dictreader(sked), header_to_fieldnames(sked), 'CSV_output.csv')