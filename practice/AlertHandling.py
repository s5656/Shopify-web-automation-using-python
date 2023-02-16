import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()

alertWindow= driver.switch_to.alert

print(alertWindow.text)
alertWindow.send_keys("Okay")
time.sleep(2)
#alertWindow.accept()
alertWindow.dismiss()

time.sleep(3)

