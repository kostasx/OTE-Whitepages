**NOTE** The API used by this script has been deprecated. Please see my latest Node.JS project [here](https://github.com/kostasx/nodejs-greek-whitepages)

Python script that submits telephone number to OTE Whitepages web page (Greece),
and retrieves name and address. Tested on Mac OS X Lion & Ubuntu 12.04.

Example usage: python ote.py <telephone number>
e.g.	       python ote.py 2102233456

Requirements:

BeautifulSoup  (Python Module)

Notes for Ubuntu Users:

1. Install BeautifulSoup => sudo apt-get install python-beautifulsoup
2. Change source code to reflect proper module importation:
	from BeautifulSoup import BeautifulSoup
