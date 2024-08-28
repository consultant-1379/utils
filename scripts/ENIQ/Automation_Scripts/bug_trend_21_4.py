from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time
import os
#import keyboard

global_filter = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/div[2]'
pf_bugs ='/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[17]/span[1]/span[1]'
tp_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[19]/span[1]/span[1]'
infra_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[14]/span[1]/span[1]'
security_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[18]/span[1]/span[1]'
inflow = '/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[6]/div[1]/div/button[1]'
turnaround = '/html/body/div[2]/div/div/div[1]/div[3]/div/div/div[6]/div[1]/div/button[6]'
period = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[3]/div/div[2]/div/div[1]/div/button/span[1]'
weekly = "//div[@class='ebComponentList-item' and text()='Weekly']"
apply = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[3]/div/div[1]/button[1]/span'
path = "H:/Downloads/"
bo_ocs_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[12]/span[1]/span[1]'
nmi_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[16]/span[1]/span[1]'
netan_bugs = '/html/body/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div/div[15]/span[1]/span[1]'


def save_image(name):
        scr = driver.find_element_by_xpath('/html/body/div[2]/div/div')
        scr.click()
        sleep(4)
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        image_path = name+'.png'
        screenshot = driver.save_screenshot(image_path)
        #crop(path+'name'+'.png')
        imageObject  = Image.open(image_path)
        if 'bug' in image_path:
                cropped = imageObject.crop((300,155,1350,510))
        if 'tat' in image_path:
                cropped = imageObject.crop((300,190,1350,540))
        cropped.save(image_path)

def click(xpath):
        button_element = driver.find_element_by_xpath(xpath)
        button_element.click()

def dos(filter, image_name):
        click(filter)
        sleep(5)
        click(inflow)
        sleep(5)
        click(filter)
        sleep(5)
        save_image(image_name+'_bugs')
        sleep(5)
        click(turnaround)
        sleep(5)
        save_image(image_name+'_tat')
        sleep(5)

def sleep(sec):
        time.sleep(sec)

def copy_to_vobs(png_name):
        png_name = "\\"+png_name;
        command = "pscp.exe -pw Naples!0512 H:\Desktop"+png_name+" esjkadm100@fem7s11-eiffel013.eiffel.gic.ericsson.se:/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Bug_Tracker_Report"
        os.system(command)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('H:\Downloads\chromedriver_win32\chromedriver.exe', options=options)
driver.get('https://pdu-oss-tools1.seli.wh.rnd.internal.ericsson.com/jirabugtracker/#jirabugtracker')
driver.implicitly_wait(10)
sleep(3)

user = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/form/div/input')
user.send_keys('zpunvai')
sleep(3)
password = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/form/div/div[1]/input')
password.send_keys('Shine##0808')
#keyboard.press_and_release('shift+s,h,i,n,e,shift+4,0,8,0,8')
sleep(3)
button = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/form/div/div[1]/button')
button.click()
sleep(5)

click(global_filter)
sleep(5)
sleep(5)
click(pf_bugs)
sleep(5)
# scr = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[4]/div/div[3]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div')
# scr.click()
# html = driver.find_element_by_tag_name('html')
# html.send_keys(Keys.END)
sleep(5)
save_image('pf_bugs')
sleep(5)
click(turnaround)
sleep(5)
click(period)
sleep(5)
click(weekly)
sleep(5)
click(apply)
sleep(5)
save_image('pf_tat')
sleep(5)
dos(tp_bugs,'tp')
dos(infra_bugs,'infra')
dos(nmi_bugs,'nmi')
dos(security_bugs,'security')
dos(bo_ocs_bugs,'bo')
dos(netan_bugs,'netan')
driver.quit()
copy_to_vobs('pf_bugs.png')
copy_to_vobs('pf_tat.png')
copy_to_vobs('tp_bugs.png')
copy_to_vobs('tp_tat.png')
copy_to_vobs('infra_bugs.png')
copy_to_vobs('infra_tat.png')
copy_to_vobs('security_bugs.png')
copy_to_vobs('security_tat.png')
copy_to_vobs('bo_bugs.png')
copy_to_vobs('bo_tat.png')
copy_to_vobs('nmi_bugs.png')
copy_to_vobs('nmi_tat.png')
copy_to_vobs('netan_bugs.png')
copy_to_vobs('netan_tat.png')