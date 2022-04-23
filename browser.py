from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def webD(url, c):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "enable-automation"])
    
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(2)
    elem = driver.find_element(By.CLASS_NAME,c)
    html = str(elem.get_attribute('innerHTML'))
    return html

def webDs(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "enable-automation"])
    
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(2)
    html = str(driver.page_source)
    return html