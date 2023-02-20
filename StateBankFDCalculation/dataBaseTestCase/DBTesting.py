import time
from StateBankFDCalculation.properties import XpathFile
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get(
    'https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
driver.maximize_window()
driver.find_element(By.XPATH, XpathFile.dismissNotificationPopupXpath).click()

connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="new_schema")

cur = connection.cursor()
cur.execute("select * from fd_calculatoins;")

for row in cur:
    principleAmount = int(row[0])
    rateOfIntrest = row[1]
    period1 = int(row[2])
    period2 = row[3]
    frequency = row[4]
    maturityValue = row[5]

    driver.find_element(By.XPATH, XpathFile.principleXpath).send_keys(principleAmount)
    driver.find_element(By.XPATH, XpathFile.rateOfIntrestXpath).send_keys(rateOfIntrest)
    driver.find_element(By.XPATH, XpathFile.timePeriod1Xpath).send_keys(period1)

    Select(driver.find_element(By.XPATH, XpathFile.timePeriod2Xpath)).select_by_visible_text(period2)
    Select(driver.find_element(By.XPATH, XpathFile.frequencyXpath)).select_by_visible_text(frequency)

    driver.find_element(By.XPATH, XpathFile.calculateButtonXpath).click()

    actualValue = driver.find_element(By.XPATH, XpathFile.maturityValueXpath).text

    if float(maturityValue) == float(actualValue):
        print("Test Case Passed")
    else:
        print("Test Case Failed")

    driver.find_element(By.XPATH, XpathFile.clearButtonXpath).click()
    time.sleep(2)

driver.quit()