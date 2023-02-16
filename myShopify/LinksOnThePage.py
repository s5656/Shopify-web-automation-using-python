from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/cart")
sleep(1)
driver.maximize_window()
print(len(driver.find_elements(By.TAG_NAME, "a")))  # total number of links on the page

driver.find_element(By.XPATH, '//*[@aria-label="Search"]/span').click()

driver.find_element(By.ID, "Search-In-Modal").send_keys("Sumit")
# driver.find_element(By.LINK_TEXT,"Search").send_keys("Sumit")

driver.find_element(By.XPATH, '//*[@class="search__button field__button"]').click()
sleep(5)

driver.close()
