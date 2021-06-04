"""
Before running the code, make sure you have installed the selenium webdriver for your browser.
Go to - https://selenium-python.readthedocs.io/installation.html -  to download and install the webdriver
"""

from selenium import webdriver
import urllib.request
from PIL import Image
import os

keyword=input('enter keyword : ')
n=int(input('how many images ? '))
url=input('enter url : ')
size=int(input('enter image size : '))


driver=webdriver.Chrome('E://Old//card//chromedriver.exe')
driver.get(url)

# provide path to dircetory before running the code
path='E://Old//cust_data'

i=1
j=1
while j<=n:

    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(i)).click()
        img=driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img')
        link=img.get_attribute('src')
        urllib.request.urlretrieve(link,path+'//'+keyword+' '+str(i)+'.jpg')

        im=Image.open(path+'//'+keyword+' '+str(i)+'.jpg')

        if im.size[0]<size and im.size[1]<size :
            im.close()
            os.remove(path+'//'+keyword+' '+str(i)+'.jpg')
        else:
            print(j,keyword+' '+str(i)+'.jpg',(im.size[0],im.size[1]))
            j+=1
        i+=1


    except:
        i+=1
        pass
