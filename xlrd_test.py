#xlrd test

import xlrd
import xlwt

#/Users/nigelharsch/Documents/programming/Music_Choice_Web_Scraper/csv_online_tester.csv

file_location =  'csv_tester.xlsx'
workbook = xlrd.open_workbook(file_location)
sheet1 = workbook.sheet_by_index(0)
print sheet1.cell_value(0,0)
print sheet1.nrows
print sheet1.ncols
