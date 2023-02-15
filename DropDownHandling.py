import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")

dropDown = Select(driver.find_element(By.XPATH, '//*[@id="input-country"]'))

time.sleep(1)

dropDown.select_by_visible_text("Malaysia")

# dropDown.select_by_value("129")
totalOptions = dropDown.options

for country in totalOptions:
    print(country.text)

print(len(totalOptions))
time.sleep(5)
