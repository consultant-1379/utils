#!/usr/bin/python

import re
import subprocess as sub
import sys,getpass, json, requests

URL='https://confluence-oss.seli.wh.rnd.internal.ericsson.com/rest/api/content'
CLI1='curl -u {usr}:{pas} -X POST -H \'Content-Type: application/json\' '
CLI2='-d \'{"type":"page","title":"%s","space":{"key":"ES"},"body":{"storage":{"value":"<p>%s <br/> </p>","representation":"storage"}}}\' '
CLI3='-d \'{"type":"page","title":"%s","ancestors":[{"id":%s}], "space":{"key":"ES"},"body":{"storage":{"value":"<p>%s <br/> </p>","representation":"storage"}}}\' '


def exe_cmd(cmd):
	output = sub.check_output(cmd, shell=True)
 	if re.search(r'.*id.+:\"(\d{9})\".*', res):
		return re.search(r'.*id.+:\"(\d{9})\".*', res).group(1)
	else:
		exit("Issue while creating the page")
	
def check_arguments():
	    """
	    Functionality : check the command line arguments
	    Return type   : Boolean
	    """
	    usage = 'usage: python Nessus_Automation.py [username] [action] [Sprint]\n\t'+\
	            'username = confluence username\n\t'+\
	            'action  = create/update'
	    if len(sys.argv) > 4: error =  'ERROR : ONLY 4 arguments allowed'
	    elif len(sys.argv) < 2: error =  'ERROR : Username not found'
	    elif len(sys.argv) < 3: error =  'ERROR : action not found'
	    elif len(sys.argv) < 4: error =  'ERROR : Sprint Release not found'
	    #elif not sys.argv[2].isdigit(): error =  'ERROR : Page ID should be integer'
	    else: return True
	    print error + '\n'+ usage
	    return False
#check_arguments()
def get_input1():
	"""
	Get the Page details 
	"""
	print "Please Select the page Type/n"/
		+"1:Parent Page\n"/
		+"2:Child page\n"/
		+"3:Exit"
	choice = raw_input("Enter your choice: ")
	if not re.search(r'1|2|3', choice):
		print "Please select the right choice"
		exit("ERROR: Input ERROR")
	elif choice == 1:
		create_parent_page()
	elif choice == 2:
		PID=raw_input("Enter the Parent ID: ")
		if not re.search(r"\d{9}", PID)
		create_child_page(PID)
	else:
		exit("Exiting as per your Choice")
def get_input2():
        """
        Get the Page details
        """
        print "Please Select the child page type/n"/
                +"1:First level Page\n"/
                +"2:Second level page\n"/
                +"3:Exit"
        choice = raw_input("Enter your choice: ")
        if not re.search(r'1|2|3', choice):
                print "Please select the right choice"
                exit("ERROR: Input ERROR")
        elif choice == 1:
		return 'pid'
        elif choice == 2:
		return 'chid'
        else:
                exit("Exiting as per your Choice")

def title_sprint_id(req):
	if req == 0:
		title = raw_input("Please Enter the title for page:\n")
		if re.search(r'(^\s+$)|^$', title):
			return title
		else:
			exit("No input given")
	elif req == 1:
		sprint = raw_input("Please Enter the sprint number:\n")
		if re.search(r'(^\s+$)|^$', sprint):
                        return sprint
                else:
                        exit("No input given")
	else:
		id = raw_input("Please Enter the:\n")
		if re.search(r'(^\s+$)|^$', id):
                        return id
                else:
                        exit("No input given")
	
def create_parent_page():
	#get the title
	title = title_sprint_id(0)
	cmd=CLI1.format(usr=USR, pas=PASSW)
	cmd = cmd + CLI2 %(title, title)+URL
	nwid = exe_cmd(cmd)
	print "Successfully created the page and page Id: %s" mwid
	opt = raw_input(" want to create child page of %s (y/n): " mwid)
	if opt == 'y':
		create_child_page(nwid)
	else:
		exit("Script exited normally")
def create_child_page(PID, *args):
	CHILD_TITLE = title_sprint_id(0)
	cmd=CLI1.format(usr=USR, pas=PASSW)
	cmd = cmd + CLI3 %(CHILD_TITLE, PID, CHILD_TITLE)+URL
	nwchid = exe_cmd(cmd)
	print "Successfully created the page and page Id: %s" nwchid
	if get_input2() == 'pid':
		create_child_page(PID)
	else:
		
if '__main__' == __name__:
	
USR=sys.argv[1]
PASSW = getpass.getpass(prompt='Enter Password: ')
