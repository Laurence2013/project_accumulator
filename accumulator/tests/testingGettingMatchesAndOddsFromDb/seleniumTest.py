from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore--ssl-errors')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + '/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)

driver.get('http://localhost:8000/index/')
print(driver.title)

time.sleep(5)
driver.close()
