__author__ = 'priyanka'
import sys
import os
if sys.platform == "win32":
    path = ".."
else:
    path = "scripts"
sys.path.append(path + '/lib')
import requestsMod
import linecache
import time
if sys.platform == "win32":
    path = ".."
else:
    path = "scripts"
sys.path.append(path + '/lib')
import ConfigParser
config = ConfigParser.ConfigParser()
config.read(path + '/etc/config.cfg')
currentPath = str(os.getcwd())
'''
download file
'''''
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requestsMod.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    f.close()
    return local_filename
'''
Print exception in more detailed format
'''
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({0}, LINE {1} "{2}"): {3}'.format(filename, lineno, line.strip(), exc_obj)
'''
Converting from epoch time to timr format
'''
def timeConvertion(FunStartTime,FunStopTime) :
    timeFormat = '%Y-%m-%d %H:%M:%S'
    exeStartTime = time.strftime(timeFormat,time.gmtime(FunStartTime/1000))
    exeStopTime = time.strftime(timeFormat,time.gmtime(FunStopTime/1000))
    return  exeStartTime,exeStopTime
'''
Function to generate Error message in case of this script failure
'''
def generateErrorMsg ():
    envList = os.environ
    emailReport = open(currentPath + '/' + str(config.get('email', 'emailReportFile')), 'w')
    buildUrl = envList['BUILD_URL'] if 'BUILD_URL' in envList else "None"
    AllureReport = buildUrl + str("allure/#/")
    emailReport.write("Hi All<br>")
    emailReport.write("Error occurred while generating EmailReport\n Please find the following details :")
    emailReport.write('Job Name: <a href=' + str(buildUrl) + '> ' + os.getenv('JOB_NAME') + '</a><br>')
    emailReport.write('Allure Report : <a href=' + str(AllureReport) + '>' + os.getenv('BUILD_NUMBER') + '</a><br>')
    emailReport.write("Regards,<br> CI Dev Infra Team")
'''
Epoch to time converted
'''
def epochToTime(epochTime):
    gmttime = time.gmtime(epochTime/1000)
    timeDate = time.strftime('%Y-%m-%d %H:%M:%S',gmttime)
    return timeDate
'''
return release from drop
'''
def getReleasefromDrop(drop):
    return 'O' + str(drop.split('.')[0] + '_' + str(drop.split('.')[1]))
'''
return product set release version from drop
'''
def getReleasefromDrop(drop):
    return str(drop.split('.')[0] + '.' + str(drop.split('.')[1]))

