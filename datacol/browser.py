
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('drivers/chromedriver')
driver.get('https://cs.ucsb.edu')
print(driver.title)
