import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

print(driver.title)

driver.quit()