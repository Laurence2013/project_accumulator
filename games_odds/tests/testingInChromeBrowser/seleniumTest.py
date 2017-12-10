from selenium import webdriver
import os
options = webdriver.ChromeOptions()
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + '/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver)

driver.get('http://www.google.com')
print(driver.title)
