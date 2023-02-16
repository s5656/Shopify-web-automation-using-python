from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

slider = driver.find_element(By.XPATH, '//*[@id="slider"]/span')

# Scrolling the page
driver.execute_script("window.scrollBy(0,800)", "")  # According to value
sleep(3)
driver.execute_script("arguments[0].scrollIntoView();", slider)  # Scroll till element is visible
sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # Ending of the page
sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")  # starting of the page
sleep(3)

ActionChains(driver).drag_and_drop_by_offset(slider, 100, 0).perform()

sleep(8)
driver.quit()
