#Script to update shipment in Jenkins Job configuration

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def click(xpath):
        button_element = driver.find_element_by_xpath(xpath)
        button_element.click()

def sleep(sec):
        time.sleep(sec)

def back_jenkins():
	jenkins_back = driver.find_element_by_xpath('//*[@id="breadcrumbs"]/li[1]/a')
	jenkins_back.click()
	sleep(3)

def add_parameter(xpath):
        wait = WebDriverWait(driver, 20)
        parameter_add = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        parameter_add.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        parameter_add.send_keys(sys.argv[1] + "_Linux")
        parameter_add.submit()
        sleep(3)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('H:\Downloads\chromedriver_win32\chromedriver.exe', options=options)
driver.get('https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/')
driver.implicitly_wait(10)
sleep(3)

user = driver.find_element_by_xpath('//*[@id="j_username"]')
user.send_keys('esjkadm100')
sleep(3)
password = driver.find_element_by_xpath('/html/body/div/div/form/div[2]/input')
password.send_keys('Naples!0512')
sleep(3)
click('/html/body/div/div/form/div[3]/input')

#KGB radiator job update start
click('//*[@id="job_KGB_Radiator"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#KGB raditor job update end

#CDB radiator job update start
click('//*[@id="job_CDB_Radiator"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#CDB raditor job update end

#Upgrade radiator job update start
click('//*[@id="job_Upgrade_Radiator"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#Upgrade raditor job update end

#Migration radiator job update start
click('//*[@id="job_Migration_Radiator"]/td[3]/a')
click('//*[@id="tasks"]/div[6]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#Migration raditor job update end

#Weekly Dashboard job update start
click('//*[@id="job_Weekly Dashboard"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#Weekly Dashboard job update end

#Weekly Smoke job update start
click('//*[@id="job_Weekly Smoke"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#Weekly Smoke job update end

#Pipeline details job update start
click('//*[@id="job_Pipeline Details"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen7"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#Pipeline details job update end

#ENIQ Stats build job update start
click('//*[@id="job_ENIQ_BUILD_LINUX_ISO_S21.4"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
add_parameter('//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')
back_jenkins()
#ENIQ Stats build job update end

#ENIQ Infra build job update start
click('//*[@id="job_ENIQ_BUILD_LINUX_ISO_I21.4"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
wait = WebDriverWait(driver, 20)
einfra_parameter_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yui-gen9"]/table/tbody/tr[6]/td[3]/textarea')))
einfra_parameter_add.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
einfra_parameter_add.send_keys(sys.argv[1])
einfra_parameter_add.submit()
sleep(3)
back_jenkins()
#ENIQ Infra build job update end

#Vapp II feature path update job start
click('//*[@id="job_ES_CDB_Vapp_NMI_21.4"]/td[3]/a')
click('//*[@id="tasks"]/div[7]/a[2]')
wait = WebDriverWait(driver, 20)
feature_path_add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yui-gen7"]/table/tbody/tr[6]/td[3]/textarea')))
feature_path_add.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
feature_path_add.send_keys("Features_21C_" + sys.argv[1] + "_Linux")
#Features_21C_21.4.8.EU2_Linux
feature_path_add.submit()
sleep(3)
back_jenkins()
#Vapp II feature path update job end

driver.quit()
