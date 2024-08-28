import os
import sys
import subprocess

args = sys.argv
rel = args[1]
ship = args[2]
server = args[3]
#pack = args[4]
fdm_version = ship[0:4]

def printme(pack):
        x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc /view/eniq_bld_'+rel+'_'+fdm_version+'.FDM/vobs/dm_eniq/AT_delivery/container/'+pack+' | grep RState', stdout=subprocess.PIPE, shell=True)
        out,err = x.communicate()
        out = out.strip()
        n = len(out)
        rstate = out[10:n-1]
        if "epfg" in pack:
                pack_new = "epfg_ft_"+rstate+".zip"
        else:
                pack_new = "RT_KGB_Delivery_"+rstate+".tar"
        if "atvts" in server:
                        d=os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no /view/eniq_bld_'+rel+'_'+fdm_version+'.FDM/vobs/dm_eniq/AT_delivery/container/'+pack+' root@'+server+'.athtem.eei.ericsson.se:/eniq/home/dcuser/'+pack_new)
        else:
                        d=os.system('sshpass -p shroot12 scp -o StrictHostKeyChecking=no /view/eniq_bld_'+rel+'_'+fdm_version+'.FDM/vobs/dm_eniq/AT_delivery/container/'+pack+' root@'+server+'.athtem.eei.ericsson.se:/eniq/home/dcuser/'+pack_new)
        if d == 0:
                        print "Copied the package to server"
        else:
                        print "Not able to copy the package to server"
                        exit(1)
#d = os.system('perl /vobs/ossrc/del-mgt/bin/RT_clean.pl '+server)
#if d == 0:
#       print "Cleared workspace successfully"
#else:
#       print "Issue in cleaning up workspace"
#       exit(1)
printme("epfg_ft.zip");
printme("RT_KGB_Delivery.tar");
