from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/cart")
sleep(1)
driver.maximize_window()
driver.find_element(by="xpath",value='//*[@id="shopify-section-header"]/sticky-header/header/div/details-modal/details/summary').click()

driver.find_element(by="xpath",value='//*[@id="Search-In-Modal"]').send_keys("Sumit")


driver.find_element(by="xpath",value='//*[@id="shopify-section-header"]/sticky-header/header/div/details-modal/details/div/div[2]/predictive-search/form/div[1]/button').click()
sleep(5)

driver.close()