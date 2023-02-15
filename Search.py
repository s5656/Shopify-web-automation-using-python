from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/cart")

driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="shopify-section-header"]/sticky-header/header/div/details-modal/details/summary').click()

driver.find_element(By.XPATH,'//*[@id="Search-In-Modal"]').send_keys("Sumit")


driver.find_element(By.XPATH,'//*[@id="shopify-section-header"]/sticky-header/header/div/details-modal/details/div/div[2]/predictive-search/form/div[1]/button').click()
sleep(5)

driver.close()