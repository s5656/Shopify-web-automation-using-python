import requests as request
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.XPATH, '//a')
countBrokeLink = 0
countValidLink = 0

for link in allLinks:
    url = link.get_attribute("href")
    try:
        req = request.head(url)
    except:
        None

    if req.status_code >= 400:
        print("Broken Link ", url)
        countBrokeLink += 1
    else:
        print("valid Link ", url)
        countValidLink += 1

print("Total Broken Links are :", countBrokeLink)
print("Total Valid Links are :", countValidLink)
