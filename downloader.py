from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve
from pyvirtualdisplay import Display
import time
import os

QUERY = input("Search Image : ")
IMAGE_RESOLUTION = input("Image Resolution : ")
NUMBER_OF_IMAGES = int(input("How many? : "))

# set these according to internet speed
WAIT_TIME_PER_IMAGE = 2
INITIAL_WAIT_TIME = 5


HEADLESS=True

SAVE_DIR = f"{QUERY.replace(' ','_')}_{NUMBER_OF_IMAGES}"


def download(query, img_num, img_res):
    """
    Auto downloads multiple images from google

    :param query: image search
    :param save_dir: image download location
    :param img_res: image resolution
                    by default medium (medium -> m)
                    large -> l ; small -> i
    """

    global WAIT_TIME_PER_IMAGE
    global INITIAL_WAIT_TIME
    global SAVE_DIR
    global HEADLESS

    # create save directory if not there
    if SAVE_DIR not in os.listdir():
        os.mkdir(SAVE_DIR)

    query = '%20'.join(query.split())

    

    # initiate webdriver
    s = Service(ChromeDriverManager().install())
    
    
    if HEADLESS: # hides webdriver browser window
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=s,options=options)
        
    else: # set HEADLESS as False otherwise
        driver = webdriver.Chrome(service=s)



    url = f'https://www.google.co.in/search?q={query}&tbm=isch&hl=en&tbs=isz:{img_res}&authuser=0&sa=X&ved=0CAIQpwVqFwoTCIiRwOri1vUCFQAAAAAdAAAAABAC&biw=1519&bih=754'
    driver.get(url)
    driver.maximize_window()
    time.sleep(INITIAL_WAIT_TIME)

    print("\ndownloading...")
    # scrape through images and download them
    for i in range(img_num):
        try:
            element = driver.find_element('xpath',
                                          f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i + 1}]/a[1]/div[1]/img')
            element.click()
            time.sleep(WAIT_TIME_PER_IMAGE)
            image = driver.find_element('xpath',
                                        '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img')
            img_src = image.get_attribute('src')
            urlretrieve(img_src, SAVE_DIR + "\\" + str(i) + '.jpg')
        except:
            pass


    print(f"\n\nDOWNLOADED {len(os.listdir(SAVE_DIR))}/{img_num} IMAGES")

download(QUERY, NUMBER_OF_IMAGES, IMAGE_RESOLUTION)
