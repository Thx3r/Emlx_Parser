 #!/usr/bin/env python
# encoding: utf-8
"""
Emlx Parser 
Base script by https://gist.github.com/5276813.git

Update By Thxer.com

"""


import email
import html2text

class Emlx(object):
    """An apple proprietary emlx message"""
    def __init__(self):
        super(Emlx, self).__init__()
        self.filename = None
        self.bytecount = 0
        self.email =  None
        self.txt = None
        self.html = None
        self.html2txt = None


    def __str__(self):
        return "Emlx Mail : %s " % (self.filename_)


    def parse(self):
        """return the data structure for the current emlx file
        * an email object
        * the plist structure as a dict data structure
        """
        with open(self.filename, "r") as f:
            # extract the bytecount
            content = f.readlines()

        if  content :
            t = open(self.filename, "rb")
            self.bytecount = int(t.readline().strip())
            # parse du mail
            self.email = email.message_from_bytes(t.read(self.bytecount))
        
        for part in self.email.walk():
            if part.get_content_type() == 'text/plain':
                self.txt = part.get_payload()            

            elif part.get_content_type() == "text/html":
                self.html = part.get_payload()
                self.html2txt = html2text.html2text(part.get_payload())


        else :
            print("Empty mail ...")
        return self.email

    def print_header(self):
        print("From : " + self.email["From"])
        print("To : " + self.email["To"])
        print("Subject : " + self.email["Subject"])
        print("Date : " + self.email["Date"])        

    def print_txt(self):
        print("--------- TXT ---------")
        print(self.txt)
        print("-----------------------")

    def print_html2txt(self):
        print("----- HTML 2 TEXT -----")
        print(self.html2txt)
        print("-----------------------")

    def print_html(self):
        print("----- HTML 2 TEXT -----")
        print(self.html)
        print("-----------------------")

if __name__ == '__main__':
    msg = Emlx()
    msg.filename = "my.emlx"
    message = msg.parse()

    msg.print_header()
    msg.print_txt()
    msg.print_html()
    msg.print_html2txt()




