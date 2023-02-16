from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")

mouseHover = driver.find_element(By.XPATH, '//*[@id="developers-menu-toggle"]/span')
users= driver.find_element(By.XPATH, '//*[@id="developers-menu-dropdown"]/li[6]/a')
act = ActionChains(driver)
act.move_to_element(mouseHover).move_to_element(users).click().perform()


sleep(8)