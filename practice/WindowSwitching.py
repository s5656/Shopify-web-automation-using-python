from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial")

element = driver.find_element(By.XPATH, '//*[@title="Accept Cookies"]')

print(element)
driver.execute_script("arguments[0].click();", element)

webElement = driver.find_element(By.XPATH, '//a[@href="https://www.facebook.com/OrangeHRM"]')
driver.execute_script("arguments[0].click();", webElement)

windowIDs = driver.window_handles

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)

driver.quit()