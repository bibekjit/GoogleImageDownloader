from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.request import urlretrieve
import time
import os

QUERY=input("Search Image : ")
IMAGE_RESOLUTION=input("Image Resolution : ")
NUMBER_OF_IMAGES=int(input("How many? : "))

WAIT=1
SAVE_DIR=f"{query.replace(" ","_")}_{NUMBER_OF_IMAGES}"

def download(query, img_num, save_dir, img_res, wait):
    """
    auto downloads multiple images from google
    
    :param query: image search
    :param save_dir: image download location
    :param img_res: image resolution
                    by default medium (medium -> m)
                    large -> l ; small -> i
    :param wait: wait time, for loading the images, in seconds. 
                            varies as per internet speed (default value = 1)
                            increase the value if internet speed is slow
                            
    
    """
    
    # create save directory if not there
    if save_dir not in os.listdir():
        os.mkdir(save_dir)
    
    query = '%20'.join(query.split())
    
    # initiate webdriver
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    url = f'https://www.google.co.in/search?q={query}&tbm=isch&hl=en&tbs=isz:{img_res}&authuser=0&sa=X&ved=0CAIQpwVqFwoTCIiRwOri1vUCFQAAAAAdAAAAABAC&biw=1519&bih=754'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    
    # scrape through images and download them
    for i in range(img_num):
        try:
            element = driver.find_element('xpath',
                                          f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i + 1}]/a[1]/div[1]/img')
            element.click()
            time.sleep(wait)
            image = driver.find_element('xpath',
                                        '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
            img_src = image.get_attribute('src')
            urlretrieve(img_src, save_dir + "\\" + str(img_num) + '.jpg')
        except:
            pass

download(QUERY,NUM_OF_IMAGES,SAVE_DIR,IMAGE_RESOLUTION,WAIT)






