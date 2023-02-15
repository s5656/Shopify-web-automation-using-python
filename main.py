from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/")

