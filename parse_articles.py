#Unbuffered CSV parser

import csv
import sys
import time
from collections import OrderedDict
import pprint
import string
import operator
import os
import datetime



def main():
	fout = open('parse_articles_output.txt', 'w')

	sources = {}
	articles = []
	
	ct = 0
	for filename in os.listdir('articles'):
		# articles.append(parse_article(filename))
		ct+=1
		# if ct == 50:
		# 	break
		# print(filename)
		pprint.pprint(parse_article(filename), fout)
		pprint.pprint("", fout)
		pprint.pprint('/'*100, fout)
		pprint.pprint("", fout)

def parse_article(path):
	f = open('articles/'+path, 'r')
	# lines = f.readlines()
	


	garbage_words = ['re:', 'vacation', 'funny', 'cute', 'cute!', 'babysitting', 'watch found', 'guys night out', 'ha ha', 'casino', 'flowers', 'text and drive', 'craft night', 'coupon club',
	 'funy', 'borrow hedge trimmer', 'home sick', 'coffee', 'employee of the month', 'picnic', 'lottery', 'holiday', 'retirement', 'birthday', 'good morning', 'cover for me',
	 'concert', 'testing 1 2 3', 'on my way', 'new gyro place', 'karoake', 'copier', 'out of staples', 'lunch', 'missing sweater']

	src = ''
	title = ''
	date = []
	secondary_date = ''
	two_dates = False
	author = ''
	text = []

	ct = 0
	for line in f:
		if line.rstrip():
			# print(line, ct)
			# if ct < 3 and 'of' in line.rstrip():
			# 	date += parse_date(line.rstrip(), path)
				# ct+=1
				# continue
			if line[0].isnumeric() and len(line) < 20:
				date.append(parse_date(line.rstrip(), path))
				ct+=1
				continue
			if ct == 0:
				src = line
			elif ct == 1:
				if line[0].isalpha():
					title = line
				else:
					ct+=1
			elif ct == 2:
				if line[0].isalpha() and len(line) < 25:
					author = line
				# else:
				# 	text.append(line.rstrip())
			# elif ct == 3:
				# if author != '':
				# 	date += parse_date(line.rstrip(),path)
				# else:
				# text.append(line.rstrip())
			else:
				text.append(line.rstrip())
			ct+=1
	if not title:
		print(path)
	return([path, src.rstrip(), title.rstrip(), author.rstrip(), date, text])
	# for row in r:
	# 	subject = row[3].lower()
		
	# 	cont = False
	# 	for word in garbage_words:
	# 		if word in subject:
	# 			cont = True
	# 			break

	# 	if cont:
	# 		continue

	# 	from_person = row[0]
	# 	to_people = row[1].split(',') 
	# 	#now by subject
	# 	if subject not in keywords:
	# 		keywords[subject] = [len(to_people), 'From: ' + row[0], 'To: ' + row[1], row[2]]

	# ordered = OrderedDict(sorted(keywords.items(), key=lambda t: t[1][0]))
	# pprint.pprint(ordered, fout)

def parse_date(s,path):
	try:
			
		splitted = s.split('/')
		if len(splitted) == 3:
			return datetime.date(int(splitted[0]), int(splitted[1]), int(splitted[2]))
		
		splitted = s.split(' of ')
		if len(splitted) == 3:
			return datetime.date(int(splitted[2]), int(month_to_num(splitted[1])), int(splitted[0]))

		splitted = s.split(' ')
		if len(splitted) == 3:
			if splitted[1][0].isalpha():
				return datetime.date(int(splitted[2]), int(month_to_num(splitted[1])), int(splitted[0]))
			else:
				print(path + ' unknown: ' + s)	
		else:
			print(path + ' unknown: ' + s)

	except TypeError as e:
		print(s,path)
		raise e

def month_to_num(month):
	return{
	        'Jan' : 1,
	        'January' : 1,
	        'Feb' : 2,
	        'February' : 2,
	        'Mar' : 3,
	        'March' : 3,
	        'Apr' : 4,
	        'April' : 4,
	        'May' : 5,
	        'Jun' : 6,
	        'June' : 6,
	        'Jul' : 7,
	        'July' : 7,
	        'Aug' : 8,
	        'August' : 8,
	        'Sep' : 9, 
	        'September' : 9, 
	        'Oct' : 10,
	        'October' : 10,
	        'Nov' : 11,
	        'November' : 11,
	        'Dec' : 12,
	        'December' : 12
	}[month]

main()