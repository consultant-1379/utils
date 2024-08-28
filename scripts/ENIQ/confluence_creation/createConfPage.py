import re
import subprocess as sub
import sys,getpass, json, requests

URL='https://confluence-oss.seli.wh.rnd.internal.ericsson.com/rest/api/content'
CLI1='curl -u {usr}:{pas} -X POST -H \'Content-Type: application/json\' '
CLI2='-d \'{"type":"page","title":"%s","space":{"id":436076545,"key":"ESD","name":"ENIQ Statistics Documentation"},"body":{"storage":{"value":"<p>%s <br/> </p>","representation":"storage"}}}\' '
CLI3='-d \'{"type":"page","title":"%s","ancestors":[{"id":%s}], "space":{"id":436076545,"key":"ESD","name":"ENIQ Statistics Documentation"}, "body":{"storage":{"value":"<p>%s <br/> </p>","representation":"storage"}}}\' '


def exe_cmd(cmd):
	output = sub.check_output(cmd, shell=True)
        #import pdb; pdb.set_trace()
 	if re.search(r'(\d{9})', output):
		return re.search(r'(\d{9})', output).group(1)
	else:
                title = re.search(r'.*title.*:\"(.*)\",.*ancestors|space.*', cmd).group(1)
                with open('error_file.txt', 'a') as errorf:
                    errorf.write(title+'\n')
		#exit("Issue while creating the page")

def create_parent_page(title, USR, PASSW):
	#get the title
	cmd=CLI1.format(usr=USR, pas=PASSW)
	cmd = cmd + CLI2 %(title, 'Created automatically')+URL
	nwid = exe_cmd(cmd)
	print "Successfully created the page and page Id: %s" % nwid
        return nwid

def create_child_page(title, PID, USR, PASSW):
	cmd=CLI1.format(usr=USR, pas=PASSW)
	cmd = cmd + CLI3 %(title, PID, 'Created automatically')+URL
	nwchid = exe_cmd(cmd)
	print "Successfully created the page and child page Id:%s  and parent id: %s" %(nwchid, PID)
        return nwchid	
	
def show():
	print 'called successfully'
#USR=sys.argv[1]
#PASSW = getpass.getpass(prompt='Enter Password: ')
