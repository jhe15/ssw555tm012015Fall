__author__="Fei Hou"

import FileOperation
import datetime

'''
Instructions:
Because the GEDCOM file generates the date type like '1 FEB 1999',
I make the function could receive that date type to compare the date.

Tips:
Use slice to cut the date.
'''
def dateBeforeCurrentDate(dataString):

	#Get today's year, month, date
	today=datetime.datetime.now()
	year=today.year
	month=today.month
	day=today.day

	#Generate a dictionary to connect the string month to month
	dic={'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,\
	'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}

	#Get the date from the string
	words=FileOperation.splitLine(dataString)
	fyear=words[2]
	fmonth=words[1]
	fday=words[0]

	#compare the provided date and the current date
	if int(fyear)>int(year):
		print 'ERROR:The date is not correct'
	elif dic[fmonth]>int(month):
		print 'ERROR:The date is not correct'
	elif int(fday)>int(day):
		print 'ERROR:The date is not correct'

#test:
#dateBeforeCurrentDate('1 DEC 2999')
