from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://whatmylocation.com/")
