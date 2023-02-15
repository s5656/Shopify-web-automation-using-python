import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

print(driver.title)
print(driver.current_url)

daysCheckBox=driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id,"day")]')
#
# for day in daysCheckBox:
#     day.click()

for day in daysCheckBox:
    selectedDays = day.get_attribute("id")
    if selectedDays=="monday" or selectedDays=="sunday":
        day.click()

print(len(driver.find_elements(By.TAG_NAME,"a")))

links=driver.find_elements(By.XPATH,'//a')

for link in links:
    print(link.text)

time.sleep(5)
