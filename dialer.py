
import re
import mechanize
from BeautifulSoup import BeautifulSoup
from CSV_input import csv_to_dictreader

def return_BStable(assetID,provider):
	'''dial BPA, search for id[:-1], return BStable'''
	#initiate modules
	br = mechanize.Browser()
	br.set_handle_robots(False)
	bs = BeautifulSoup

	# navigate and populate
	br.open("http://bpa2.indemand.com/package-search/") #nav to search page
	br.select_form(nr=0) #selects form, focuses
	br['assetID'] = assetID[-8:-1]  #sets assedID less last digit
	br['provider'] = "MUSIC_CHOICE" #sets sched harcoded

	#submit and read
	rs = br.submit()
	html = rs.read()
	soup = BeautifulSoup(html)
	table = soup.find("table")

	if table:
		return table
	return False

def BStable_to_dict(BStable):
	table = BStable
	dict_list = []
	
	for row in table.findAll('tr')[1:]: #removes header
	    col = row.findAll('td')
	    date = col[0].string
	    asset_id = col[2].string
	    asset_name = col[1].string
	    dict_list.append(
	    	{'Package Creation Date' : date, 'Asset Name' : asset_name, 'Asset ID' : asset_id}
	    	)
	return dict_list

def return_BSdict(assetID,provider):
	BPA_response = return_BStable(assetID, provider)	
	if BPA_response:
		BPA_response = BStable_to_dict(BPA_response)
		for row in BPA_response:
			if row['Asset ID'][-8:] == assetID[-8:]:
				return BPA_response
		return False
	return False

def BStable_to_csv(table):
	csv =""
	header = table.findAll('th')
	asset_name = header[3].text
	date = header[0].text
	asset_id = header[2].text
	csv += date+","+asset_id+","+asset_name+",\n"
	for row in table.findAll('tr')[1:]: #keeps header
	    col = row.findAll('td')
	    asset_name = col[3].text
	    date = col[0].string.replace(',', '')
	    asset_id = col[2].string
	    csv += date+","+asset_id+","+asset_name+",\n"
	return csv

def return_dict_list(asset_id, provider):
	'''dial, search, return list of dicts'''
	#initiate modules
	br = mechanize.Browser()
	br.set_handle_robots(False)
	bs = BeautifulSoup

	# vanigate and populate
	br.open("http://bpa2.indemand.com/package-search/") #nav to search page
	br.select_form(nr=0) #selects form, focuses
	br['assetID'] = assetID  #sets assedID
	br['provider'] = "MUSIC_CHOICE" #sets sched harcoded

	#submit and read
	rs = br.submit()
	html = rs.read()
	soup = BeautifulSoup(html)
	table = soup.find("table")

	return BStable_to_dict(table)

def return_csv(asset_id, provider):
	'''dial, search, return csv'''
	#initiate modules
	br = mechanize.Browser()
	br.set_handle_robots(False)
	bs = BeautifulSoup

	# navigate and populate
	br.open("http://bpa2.indemand.com/package-search/") #nav to search page
	br.select_form(nr=0) #selects form, focuses
	br['assetID'] = assetID  #sets assedID
	br['provider'] = "MUSIC_CHOICE" #sets sched harcoded

	#submit and read
	rs = br.submit()
	html = rs.read()
	soup = BeautifulSoup(html)
	table = soup.find("table")

	return BStable_to_csv(table)



if __name__ == "__main__":
	assetID = "MCPK2000000000402212" #strips preamble and last digit
	provider = "MUSIC_CHOICE"

	print return_BSdict(assetID,provider)

	# table = return_BStable(assetID, provider)
	# print type(table)


	# response = []

	# #search table and populate columms
	# for row in table.findAll('tr')[1:]:
	#     col = row.findAll('td')
	#     date = col[0].string
	#     asset_id = col[2].string
	#     asset_name = col[1].string
	#     response.append(
	#     	{"Date" : date, "asset_name" : asset_name, "asset_id" : asset_id}
	#     	)
	# print response
#here's the submit form
# '''
# csrfmiddlewaretoken:973cb199cb58e4c66f442b70843295bb
# assetName:
# title:
# assetID:
# rowCreationTime:
# dateDirection:gte
# studioName:
# provider:MUSIC_CHOICE
# licStartDate:
# licStartDateDirection:gte
# licEndDate:
# licEndDateDirection:gte
# processingID:Any
# '''

