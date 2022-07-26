from bs4 import BeautifulSoup as bs
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://moonarch.app/miners'

def get_miners_list():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    # driver.implicitly_wait(10)
    driver.get(url)

    el_button = WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CLASS_NAME, 'bottom-action-bar'))
    el_button.click()
    
    el_button = WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CLASS_NAME, 'table-pin'))
    
    html = driver.page_source
    driver.close()
    soup = bs(html, 'html.parser')
    
    el = soup.select('table#__BVID__68 tr > td:nth-of-type(2) > a')
    
    group_list = []
    for e in el:
        group_list.append(e.text)

    return group_list


get_miners_list()