#!/usr/bin/env python
# coding: utf-8

import re
import csv

#This bit of code removes duplication in the list of text objects
reader = csv.reader(open('all_text_object_id.txt', 'r'), delimiter='\t')
out_file_name = 'unique_list.txt'
out_file = open(out_file_name, 'w')

taxon_id = set()
for row in reader:
	if row[2] not in taxon_id:
		out_file.write('\t'.join(row) + '\n')
out_file.close()

#This bit of code looks for relevant keywords		
in_file_name = 'unique_list.txt'
in_file = open(in_file_name, 'r')
out_file_name = 'target_text.txt'
out_file = open(out_file_name, 'w')

for line in in_file:
	row = line.split('\t')
	taxon = row[0]
	text_id = row[2]
	text = row[3]
	m = re.search('length', text)
	if m != None:
		print 'Size data present'
		out_file.write('\t'.join([taxon,'size',text_id,text + '\n']))
	else:
		print 'No size data'
	m = re.search('clutch|egg', text)
	if m != None:
		print 'Clutch or ova size data present'
		out_file.write('\t'.join([taxon,'clutch size',text_id,text + '\n']))
	else:
		print 'No clutch or ova size data'
	m = re.search('development|reproduction', text)
	if m != None:
		print 'Life history data present'
		out_file.write('\t'.join([taxon,'life history',text_id,text + '\n']))
	else:
		print 'No life history data'
	m = re.search('hibernation|breeding', text)
	if m!= None:
		print 'Habitat use data present'
		out_file.write('\t'.join([taxon,'life history',text_id,text + '\n']))
	else:
		print 'No habitat use data'
	m = re.search('occur|range|inhabit|found',text)
	if m != None:
		print 'Distribution data present'
		out_file.write('\t'.join([taxon,'distribution',text_id,text + '\n']))
	else:
		print 'No distribution data'
	m = re.search('precipitation|arid|wet|dry|moist',text)
	if m != None:
		print 'Precipitation data present'
		out_file.write('\t'.join([taxon,'precipitation',text_id,text + '\n']))
	else:
		print 'No precipitation data'
	m = re.search('temperature|temperate|tropic',text)
	if m != None:
		print 'Temperature data present'
		out_file.write('\t'.join([taxon,'temperature',text_id,text + '\n']))
	else:
		print 'No temperature data'
