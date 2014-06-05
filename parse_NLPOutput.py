#Unbuffered CSV parser

import sys
from collections import OrderedDict
import pprint
import string
import operator
import os
import re

# This script is to map filenames to related people's names

# get value by tag
def getValue(buf , str): # buf is curren line, str is the tag
	return re.sub('<.*?>','', buf).strip()

# Unit example
# <token id="1">
#             <word>The</word>
#             <lemma>the</lemma>
#             <CharacterOffsetBegin>0</CharacterOffsetBegin>
#             <CharacterOffsetEnd>3</CharacterOffsetEnd>
#             <POS>DT</POS>
#             <NER>O</NER>
#             <Speaker>PER0</Speaker>
# </token>
 
def parse_xml(path):
	f = open('nlpxmloutput/'+str(path)+".xml", 'r')
	info = []
	personName = [] 
	organization = []
	location = []
	buffer = []
	for l in f:
		if '<token' in l:
			Word = f.next()
			Lemma = f.next()
			f.next() 	#offsetBegin
			f.next()	#offsetEnd
			f.next()	#POS
			Ner = f.next()
			ner =  getValue(l, 'NER')
			if 'PERSON' in Ner:
				name = getValue(Word, 'word')
				if name not in personName:
					personName.append(name)
			# elif 'LOCATION' in Ner:
			# 	loc = getValue(Word, 'word')
			# 	if loc not in location:
			# 		location.append(loc)
			# elif 'ORGANIZATION' in Ner:
			# 	org = getValue(Word, 'word')
			# 	if org not in organization:
			# 		organization.append(org)
	# info = [path, personName, organization, location]
	# return str(info)
	return str(personName)

def main():
	fout = open('ppl_in_articles.txt', 'w')

	sources = {}
	articles = []
	
	ct = 0
	for filename in os.listdir('nlpxmloutput'):
		pprint.pprint(str(ct) + parse_xml(ct), fout)
	# 	# articles.append(parse_article(filename))
		ct+=1
		# if ct == 50:
		# 	break
		# print(filename)
		# pprint.pprint(parse_article(filename), fout)
		# pprint.pprint("", fout)
		# pprint.pprint('/'*100, fout)
		# pprint.pprint("", fout)

# def parse_article(path):
# 	f = open('articles/'+path, 'r')
# 	# lines = f.readlines()
	


# 	garbage_words = ['re:', 'vacation', 'funny', 'cute', 'cute!', 'babysitting', 'watch found', 'guys night out', 'ha ha', 'casino', 'flowers', 'text and drive', 'craft night', 'coupon club',
# 	 'funy', 'borrow hedge trimmer', 'home sick', 'coffee', 'employee of the month', 'picnic', 'lottery', 'holiday', 'retirement', 'birthday', 'good morning', 'cover for me',
# 	 'concert', 'testing 1 2 3', 'on my way', 'new gyro place', 'karoake', 'copier', 'out of staples', 'lunch', 'missing sweater']

# 	src = ''
# 	title = ''
# 	date = []
# 	secondary_date = ''
# 	two_dates = False
# 	author = ''
# 	text = []

# 	ct = 0
# 	for line in f:
# 		if line.rstrip():
# 			# print(line, ct)
# 			# if ct < 3 and 'of' in line.rstrip():
# 			# 	date += parse_date(line.rstrip(), path)
# 				# ct+=1
# 				# continue
# 			if line[0].isnumeric() and len(line) < 25:
# 				date.append(parse_date(line.rstrip(), path))
# 				ct+=1
# 				continue
# 			if ct == 0:
# 				src = line
# 			elif ct == 1:
# 				if line[0].isalpha():
# 					title = line
# 				else:
# 					ct+=1
# 			elif ct == 2:
# 				if line[0].isalpha() and len(line) < 25:
# 					author = line
# 				# else:
# 				# 	text.append(line.rstrip())
# 			# elif ct == 3:
# 				# if author != '':
# 				# 	date += parse_date(line.rstrip(),path)
# 				# else:
# 				# text.append(line.rstrip())
# 			else:
# 				text.append(line.rstrip())
# 			ct+=1
# 	if not title:
# 		print(path + ' has no title')
	# rvalue = [path, src, ]
	# return(rvalue)
# 	return([path, src.rstrip(), title.rstrip(), author.rstrip(), date, text])
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

# def parse_date(s,path):
# 	try:
			
# 		splitted = s.split('/')
# 		if len(splitted) == 3:
# 			return datetime.date(int(splitted[0]), int(splitted[1]), int(splitted[2]))
		
# 		splitted = s.split(' of ')
# 		if len(splitted) == 3:
# 			return datetime.date(int(splitted[2]), int(month_to_num(splitted[1])), int(splitted[0]))

# 		splitted = s.split(' ')
# 		if len(splitted) == 3:
# 			if splitted[1][0].isalpha():
# 				return datetime.date(int(splitted[2]), int(month_to_num(splitted[1])), int(splitted[0]))
# 			else:
# 				print(path + ' unknown: ' + s)	
# 		elif len(splitted) > 3:
# 			# for x in range(0,3):
# 			# 	if not splitted[x]:
# 			# 		splitted.remove(x)
# 			splitted.remove('')
# 			# splitted.remove(' ')
# 			if splitted[1][0].isalpha():
# 				return datetime.date(int(splitted[2]), int(month_to_num(splitted[1])), int(splitted[0]))
# 		elif len(splitted) == 2:
# 			if splitted[0][2].isalpha() and splitted[0][1].isnumeric():
# 				return datetime.date(int(splitted[1]), int(month_to_num(splitted[0][2:])), int(splitted[0][0:2]))
		
# 		else:
# 			print(path + ' unknown: ' + s)

# 	except TypeError as e:
# 		print(s,path)
# 		raise e


main()



# parse_xml("1.xml")