import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
#Find the number of rows and column
noOfRows = len(driver.find_elements(By.XPATH, '//*[@name="BookTable"]//tr'))
print("No of Rows are",noOfRows)
noOfColumns = len(driver.find_elements(By.XPATH, '//*[@name="BookTable"]//tr[1]/th'))
print("No of Rows are", noOfColumns)
#Print all the data from the table
for row in range(2,noOfRows+1):
    for column in range(1,noOfColumns+1):
        texts = driver.find_element(By.XPATH, '//*[@name="BookTable"]//tr['+str(row)+']/td['+str(column)+']').text
        print(texts,end="  ")
    print()
print("-------------")
#Print the data from the table where if price is above 500
for row in range(2,noOfRows+1):
    price = driver.find_element(By.XPATH, '//*[@name="BookTable"]//tr['+str(row)+']/td[4]').text
    if int(price) > 300:
        print(driver.find_element(By.XPATH, '//*[@name="BookTable"]//tr['+str(row)+']').text)

