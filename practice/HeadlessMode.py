from selenium import webdriver

headlessMode = webdriver.ChromeOptions()
# headlessMode.headless=True
headlessMode.add_argument('--headless')

driver = webdriver.Chrome(options=headlessMode)

driver.get('https://www.youtube.com/')

driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.name)
print(driver.current_window_handle)

driver.close()