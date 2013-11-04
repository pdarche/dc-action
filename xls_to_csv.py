import xlrd
import csv
import sys


workbook = sys.argv[1]
sheet = sys.argv[2]
filename = sys.argv[3]

def csv_from_excel():
	out_file = 'data/csvs/%s.csv' % filename
	wb = xlrd.open_workbook(workbook)
	sh = wb.sheet_by_name(sheet)
	your_csv_file = open(out_file, 'wb')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

	for rownum in xrange(sh.nrows):
		wr.writerow(sh.row_values(rownum))
	
	your_csv_file.close()

csv_from_excel()