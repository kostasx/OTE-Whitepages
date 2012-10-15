#!/usrc/bin/python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import urllib2

if len(sys.argv) < 2:
	print "Usage: python ote.py <number>"
	print "Example: python ote.py 2108822508"
	exit()
url = 'http://11888.ote.gr/web/guest/white-pages/search?who='+sys.argv[1]+'&where='
res = urllib2.urlopen(url)
html = res.read()

soup = BeautifulSoup(html)

content = soup.find('div', { 'class' : 'results-list'}).findNext('div', {'class':'details'})
name = content.find('h3').getText().strip()
addr = content.find('div', { 'class' : 'summary'}).next.strip()
tel = content.find('div', {'class':'phone'}).getText().strip()
print "\n"
print "Name: \t\t" + name
print "Address: \t" + addr
print "Tel.: \t\t" + tel
print "\n"
