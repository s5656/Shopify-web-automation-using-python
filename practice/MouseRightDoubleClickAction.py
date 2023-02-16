from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.guru99.com/test/simple_context_menu.html')

rightClick= driver.find_element(By.XPATH, '//*[@id="authentication"]/span')

act = ActionChains(driver)
act.context_click(rightClick).perform()
driver.find_element(By.XPATH, '//*[@id="authentication"]/ul/li[7]/span').click()
driver.switch_to.alert.accept()       #Accept alert
sleep(3)

doubleClick= driver.find_element(By.XPATH, '//*[@id="authentication"]/button')
act.double_click(doubleClick).perform()
driver.switch_to.alert.accept()       #Accept alert

sleep(8)