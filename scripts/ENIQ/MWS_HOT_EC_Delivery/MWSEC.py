# ***********************************************************************************
# Author: Priyanka Samikannu                                                                    *
# Description: This script will                                                                 *
#                   * Read input from user via Jenkin job                           *
#                   * Convert them into Ericsson standard MWS EC delivery format    *
#                   * Generate HTML file                                                                        *
# ***********************************************************************************
#import sys
from subprocess import *
import os

ship = os.environ['SHIPMENT']
rstate = os.environ['R_STATE']
ecno = os.environ['EC_NO']
product = os.environ['PRODUCT']
request = os.environ['REQUESTER']
reason = os.environ['REASON']
deploy = os.environ['DEPLOYMENT']
gasks = os.environ['GASK_LINK']
readme = os.environ['README']
slogan = os.environ['SLOGAN']
docname = os.environ['DOC_NAME']
document = os.environ['DOC_LINK']
update = os.environ['UPDATE']
note = os.environ['NOTE']
if len(update)>5 and len(note)>5:
        strTable = "<!DOCTYPE html><html><head><style>body{color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;line-height: 80%;mso-line-height-rule: exactly;}th{color: maroon;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}td{color: #961296;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}h6{color: #961296;font-size: 10.0pt;text-align: left;font-family: Segoe UI;}ol{color: blue;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;padding-left:3em;line-height: 80%;mso-line-height-rule: exactly;}</style></head><body><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>Update: "+update+"</p><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>Note: "+note+"</p><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>PRELIM Release Mail: HOT ENIQ Packages for ENIQ Statistics "+ship+" "+rstate+" MWS EC"+ecno+" Release</p><table>"
elif len(update)>5 and len(note)<5:
        strTable = "<!DOCTYPE html><html><head><style>body{color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;line-height: 80%;mso-line-height-rule: exactly;}th{color: maroon;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}td{color: #961296;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}h6{color: #961296;font-size: 10.0pt;text-align: left;font-family: Segoe UI;}ol{color: blue;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;padding-left:3em;line-height: 80%;mso-line-height-rule: exactly;}</style></head><body><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>Update: "+update+"</p><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>PRELIM Release Mail: HOT ENIQ Packages for ENIQ Statistics "+ship+" "+rstate+" MWS EC"+ecno+" Release</p><table>"
elif len(note)>5 and len(update)<5:
        strTable = "<!DOCTYPE html><html><head><style>body{color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;line-height: 80%;mso-line-height-rule: exactly;}th{color: maroon;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}td{color: #961296;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}h6{color: #961296;font-size: 10.0pt;text-align: left;font-family: Segoe UI;}ol{color: blue;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;padding-left:3em;line-height: 80%;mso-line-height-rule: exactly;}</style></head><body><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>Note: "+note+"</p><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>PRELIM Release Mail: HOT ENIQ Packages for ENIQ Statistics "+ship+" "+rstate+" MWS EC"+ecno+" Release</p><table>"
else:
        strTable = "<!DOCTYPE html><html><head><style>body{color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;line-height: 80%;mso-line-height-rule: exactly;}th{color: maroon;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}td{color: #961296;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;text-align: left;}h6{color: #961296;font-size: 10.0pt;text-align: left;font-family: Segoe UI;}ol{color: blue;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;padding-left:3em;line-height: 80%;mso-line-height-rule: exactly;}</style></head><body><p style='color: red;font-family: Tahoma;font-weight: bold;font-size: 10.0pt;'>PRELIM Release Mail: HOT ENIQ Packages for ENIQ Statistics "+ship+" "+rstate+" MWS EC"+ecno+" Release</p><table>"
pro = product.split("$")
if len(pro)==1:
        strRW = "<tr style='height: 20px'><th>Product Delivery information:</th><th>&nbsp;&nbsp;&nbsp;</th><th>"+product+"</th></tr>";
        strTable = strTable+strRW
elif len(pro)>1:
        for num in pro:
                if pro.index(num) == 0:
                        strRW = "<tr style='height: 20px'><th style ='color: maroon;'>Product Delivery information:</th><th>&nbsp;&nbsp;&nbsp;</th><th>"+num+"</th></tr>";
                        strTable = strTable+strRW
                else:
                        strRW = "<tr style='height: 20px'><td></td><td>&nbsp;&nbsp;&nbsp;</td><td style ='color: maroon;'>"+num+"</td></tr>";
                        strTable = strTable+strRW
strRW = "<tr style='height: 25px'><td>Requester:</td><td>&nbsp;&nbsp;&nbsp;</td><td>"+request+"</td></tr><tr style='height: 25px'><td>Reason:</td><td>&nbsp;&nbsp;&nbsp;</td><td>Correction of JIRA "+reason+"</td></tr><tr style='height: 25px'><td>Deployment:</td><td>&nbsp;&nbsp;&nbsp;</td><td>"+deploy+"</td></tr></table><h6 style='font-weight: normal;'><strong>Recommendation: </strong>This EC should be loaded onto the server on O&M media for installing MWS. Refer to the accompanying read-me file for instructions</h6><ol type='1'><li>Download Information:</li>";
strTable = strTable+strRW
gask = gasks.split("$")
for num in pro:
        x = num.split("_R", 1)
        strRW = "<p style ='color: maroon;font-weight:normal;'>"+x[0]+": <a  href="+gask[pro.index(num)]+">"+gask[pro.index(num)]+"</a></p>";
        strTable = strTable+strRW
strRW = "<li>Readme:</li><p><a style='font-weight:normal;' href="+readme+">"+readme+"</a></p>";
strTable = strTable+strRW
doc = document.split("$")
docnm = docname.split("$")
if len(document)>10:
    strRW = "<p class='big'></p><li>Document</li>";
    strTable = strTable+strRW
    for d in docnm:
        strRW = "<p style ='color: maroon;font-weight:normal;'>"+d+": <a href="+doc[docnm.index(d)]+">"+doc[docnm.index(d)]+"</a></p>";
        strTable = strTable+strRW
strRW = "<li>Included TR/JIRA Fixes:</li><p><table style='width:65%; height: 10%;color:maroon;'><tr><th style ='color: maroon;'>JIRA Number</th><th>&nbsp;&nbsp;&nbsp;</th><th>Slogan</th></tr>";
strTable = strTable+strRW
jira = reason.split(",")
slog = slogan.split("$")
for jr in jira:
        strRW = "<tr><td style ='color: maroon;font-weight:normal;height: 10px;'>"+jr+"</td><td>&nbsp;&nbsp;&nbsp;</td><td style ='color: maroon;font-weight:normal;'>"+slog[jira.index(jr)]+"</td></tr>";
        strTable = strTable+strRW

strTable = strTable+"</table></p></ol></body></html>"

hs = open("MWSEC.html", 'w')
hs.write(strTable)