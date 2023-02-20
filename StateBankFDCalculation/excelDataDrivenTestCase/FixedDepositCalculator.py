from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from StateBankFDCalculation.properties import XpathFile
from StateBankFDCalculation.excelDataDrivenTestCase import ExcelUtilities

driver = webdriver.Chrome()

driver.get(
    'https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
driver.maximize_window()
driver.find_element(By.XPATH, XpathFile.dismissNotificationPopupXpath).click()

file = "//Users//testvagrant//Downloads//TestCase.xlsx"
row_count = ExcelUtilities.getRowCount(file, "Sheet1")

for row in range(2, row_count + 1):
    principleAmount = int(ExcelUtilities.readData(file, "Sheet1", row, 1))
    rateOfIntrest = ExcelUtilities.readData(file, "Sheet1", row, 2)
    period1 = int(ExcelUtilities.readData(file, "Sheet1", row, 3))
    period2 = ExcelUtilities.readData(file, "Sheet1", row, 4)
    frequency = ExcelUtilities.readData(file, "Sheet1", row, 5)
    maturityValue = ExcelUtilities.readData(file, "Sheet1", row, 6)

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

