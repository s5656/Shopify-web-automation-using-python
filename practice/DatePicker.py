from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

month="June"
day ="4"
year ="2025"
driver.switch_to.frame(0)
driver.find_element(By.XPATH, '//*[@id="datepicker"]').click()

while True:
    mon = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-month"]').text
    yr = driver.find_element(By.XPATH, '//*[@class="ui-datepicker-year"]').text
    if mon==month and yr ==year:
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()

sleep(2)
dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for ele in dates:
    if ele.text == day:
        ele.click()
        break

sleep(5)

