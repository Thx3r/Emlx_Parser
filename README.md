# Emlx_Parser
Simple way to parse emlx to email object


** Requierement  / Install**

	pip3 install --user html2text
	git clone https://github.com/Thx3r/Emlx_Parser.git

** Edit and lauch **

Change "my.emlx" by the emlx file name
__Run it !__

	python3.4  Emlx-Parser.py

		
		From : a@fakemeail.com
		To : b@fakemeail.com
		Subject : EXEMPLE
		Date : Mon, 3 Aug 2015 10:12:38 +0200
		--------- TXT ---------
		Fake txt content
		
		-----------------------
		----- HTML 2 TEXT -----
		This is Html
		-----------------------
		----- HTML 2 TEXT -----
		<b>This is Html</b>
		-----------------------

