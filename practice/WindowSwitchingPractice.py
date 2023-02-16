import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, '//a[@href="https://www.facebook.com/OrangeHRM/"]').click()

windowIDs = driver.window_handles

for winID in windowIDs:
    driver.switch_to.window(winID)
    print(driver.title)

driver.quit()

