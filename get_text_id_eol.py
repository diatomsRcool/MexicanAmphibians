#!/usr/bin/env python
# coding: utf-8

from __future__ import division
import urllib, json, re
from bs4 import BeautifulSoup

in_file_name = "all_taxon_id.txt"
in_file = open(in_file_name, 'r')
out_file_name = "all_text_object_id.txt"
out_file = open(out_file_name, 'w')

def data_object_url(id):
    return 'http://eol.org/api/pages/1.0/' + id.strip() + '.json?images=0&videos=0&sounds=0&maps=0&text=75&iucn=false&subjects=distribution|habitat|size|lifecycle|reproduction&licenses=all&details=true&common_names=false&synonyms=false&references=false&vetted=0&cache_ttl='


counter = 0

for line in in_file:
	print counter
	row = line.split(',')
	tax_name = row[0]
	tax_id = row[1].strip()
	results = urllib.urlopen(data_object_url(tax_id)).read()
	print line
	data = json.loads(results)
	if data ['dataObjects'] == []:
		print 'No Data'
	else:
		text_list = []
		text_list = data ['dataObjects']
		for object in text_list:
			text_id = object['identifier']
			text = object['description']
			p = re.compile('<br>')
			m = p.sub(' ',text)
			soup = BeautifulSoup(m)
			clean = soup.get_text()
			ready = clean.encode('utf8')
			p = re.compile('\n')
			ready_text = p.sub(' ',ready)
			out_file.write('\t'.join([tax_name,tax_id,str(text_id),ready_text + '\n']))
	counter = counter + 1																																										
in_file.close()																							
out_file.close()