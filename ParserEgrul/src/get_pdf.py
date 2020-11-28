from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from parsel import Selector

import time
from pathlib import Path
import urllib
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": os.path.join(os.getcwd(), 'tmp')})
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
# Установить ChromeDriver соответсвующей версии Google Chrome в C:/Program Files/chromedriver/ 
# В архиве ChromeDriver версии 86.0.4240.22 
driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver/chromedriver.exe', options=options)
sel = Selector(text=driver.page_source)

url = 'https://egrul.nalog.ru/index.html'

def enter():
    global driver, sel, url
    driver.get(url)
    sel = Selector(text=driver.page_source)

def close():
    global driver
    driver.close()

# Стоит оговорится, что если дается имя, то скачивается первый pdf

def paste_id_or_name_and_get_pdf(id_or_name):
    global driver
    driver.find_element_by_id('query').send_keys(id_or_name)
    driver.find_element_by_id('btnSearch').click()
    time.sleep(3)
    driver.find_elements_by_xpath('/html/body//div[3]/button')[0].click()

def get_pdf(id_or_name):
    enter()
    path = os.path.join(os.getcwd(), 'tmp')
    for e in os.listdir(path):
        try:
            os.remove(os.path.join(path, e))
        except Exception:
            raise('Закройте все открытые pdf-ники в папке tmp')
    paste_id_or_name_and_get_pdf(id_or_name)
    time.sleep(3)
    close()
    os.rename(os.path.join(path, os.listdir(path)[0]), os.path.join(path, 'temp.pdf'))
        
if __name__ == "__main__":
     get_pdf('ВАРЛАМОВ ИЛЬЯ АЛЕКСАНДРОВИЧ')
