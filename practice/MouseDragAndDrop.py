from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
sleep(2)

drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(drag,drop).perform()

dragJohn=driver.find_element(By.XPATH, '//*[@id="gallery"]/li[1]/img')
dragMary=driver.find_element(By.XPATH, '//*[@id="gallery"]/li[2]/img')

droper = driver.find_element(By.XPATH, '//*[@id="trash"]')

ActionChains(driver).drag_and_drop(dragJohn,droper).perform()

ActionChains(driver).drag_and_drop(dragMary, droper).perform()

sleep(10)

