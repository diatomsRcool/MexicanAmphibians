#!/usr/bin/env python
# coding: utf-8

from __future__ import division
import urllib
import json

in_file_name = "Mex_Amph_species.csv"
in_file = open(in_file_name, 'r')
out_file_name = "all_taxon_id.txt"
out_file = open(out_file_name, 'w')

def data_object_url(line):
    return 'http://eol.org/api/search/1.0.json?q=' + line.strip() + '&page=1&exact=true'

counter = 0

for line in in_file:
	print counter
	results = urllib.urlopen(data_object_url(line)).read()
	print line
	data = json.loads(results)
	if data ['results'] == []:
		print 'No Data'
	else:
		eol_taxon_id = data ['results'][0]['id']
	counter = counter + 1
	out_file.write(','.join([line.strip(),str(eol_taxon_id) + '\n']))																																										
in_file.close()																							
out_file.close()