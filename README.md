# Emlx_Parser
Simple way to parse emlx to email object


** Requierement  / Install**

	pip3 install --user html2text
	git clone https://github.com/Thx3r/Emlx_Parser.git

** Edit and lauch **

Change "my.emlx" by the emlx file name
__Run it !__

	python3.4  Emlx-Parser.py

		
	usage: Emlx-Parser.py [-h] [--html] [--txt] [--html2txt] [--json] [--head]
	                      file [file ...]
	
	Parser for emlx mail files
	
	positional arguments:
	  file        Emlx mail file
	
	optional arguments:
	  -h, --help  show this help message and exit
	  --html      Get html content
	  --txt       Get txt content
	  --html2txt  Get html content in text format
	  --json      Get all in json
	  --head      Get head summary

