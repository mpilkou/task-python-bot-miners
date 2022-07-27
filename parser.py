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

    button_element = WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CLASS_NAME, 'bottom-action-bar'))
    button_element.click()
    
    WebDriverWait(driver, 20).until(lambda d: d.find_element(By.CLASS_NAME, 'table-pin'))
    
    html = driver.page_source
    driver.close()
    soup = bs(html, 'html.parser')
    
    mainers_elements_resultset = soup.select('table#__BVID__68 tr > td:nth-of-type(2) > a')
    
    mainers_group_list = []
    for e in mainers_elements_resultset:
        mainers_group_list.append(e.text)

    return mainers_group_list


get_miners_list()