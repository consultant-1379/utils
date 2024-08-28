#!/usr/bin/python
import re
import os
import sys
import getpass
import xml.dom.minidom
#custom Module
import createConfPage as conf
from random import randint as rint
#Remove error file
os.remove('error_file.txt') if os.path.exists('error_file.txt') else None
#Ge the password
PASSWD = getpass.getpass('Enter the password for zpunvai :' )
#gettign xml file
xmlfile=sys.argv[1]  if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else exit('ERROR: No file provied/No file found')
#XML parser
DOMTree = xml.dom.minidom.parse(xmlfile)
collection = DOMTree.documentElement
body = collection.getElementsByTagName("body")
def chl_tag(chl, tmp):
#    import pdb; pdb.set_trace()
    tit = ''
    for i in chl.childNodes:
        if "title" in str(i):
	    for chlnode in i.childNodes:
                tit = chlnode.data
		tmp[tit]=[]
            continue
        if 'chl' in str(i):
            tmp[tit].append(chl_tag(i, {}))
            continue
        if 'table' in str(i):
	    table = table_form(i) 
            tmp[tit]+=table
            continue
    return tmp
def table_form(table):
    table1 = []
    for tp in table.getElementsByTagName("tp"):
        table1.append(tp.childNodes[0].data)          
    return table1

def create_confpage(page_dtails, pid=None):
    # conf
    for i in page_dtails.keys():
       #import pdb; pdb.set_trace()
       print i, "Creating page"
       if pid:
           PID = conf.create_child_page(i.replace('\n', ' '), pid, 'zpunvai', PASSWD)
       else:
           PID = conf.create_parent_page(i.replace('\n', ' '), 'zpunvai', PASSWD)
       if type(page_dtails[i]) == list:
           for subele in page_dtails[i]:
		if type(subele) == dict:
                    create_confpage(subele, PID)
		    continue
		if subele[0].isdigit(): continue
		if subele == ' ': continue
		#exit('exited as per wish')
                print subele, "Creating child page"
		conf.create_child_page(subele.replace('\n', ' '), PID, 'zpunvai', PASSWD)
        
for bdy in body:
    for i in body[0].childNodes:
        if 'chl' in str(i):
	    print chl_tag(i, {})
            #create_confpage(chl_tag(i, {}))
if os.path.isfile('error_file.txt'):
    print "\n#########################"
    print 'Found dublicate Entries\n'
    print "#########################"
    with open('error_file.txt', 'r') as errorf:
        for i in errorf.read().splitlines():
            print i, ' --> Dublicate entry found'
    exit(1)
else:
   print "Executed Successfully"
   exit(0)
