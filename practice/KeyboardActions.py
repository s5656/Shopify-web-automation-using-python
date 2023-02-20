import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="inputText1"]').send_keys("Welcome to text Compare")
driver.find_element(By.XPATH, '//*[@id="inputText2"]')

ActionChains(driver).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

driver.find_element(By.XPATH, '//*[@class="compareButtonText"]').click()

time.sleep(8)

