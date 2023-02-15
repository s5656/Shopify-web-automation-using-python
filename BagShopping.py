from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/")
driver.find_element(By.XPATH,'//*[@id="Banner-template--16876710920493__image_banner"]/div[2]/div/div[2]/a').click()

driver.find_element(By.XPATH,'//*[@id="title-template--16876710854957__product-grid-8002225537325"]').click()

driver.find_element(By.XPATH,'//*[@id="product-form-template--16876710887725__main"]/div/div/div/div/div/button[1]').click()

driver.implicitly_wait(2)
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('sumitchavan5473@gmail.com')

driver.find_element(By.XPATH,'//*[@id="marketing_opt_in"]').click()

driver.find_element(By.XPATH,'//*[@id="TextField0"]').send_keys('Sumit')

driver.find_element(By.XPATH,'//*[@id="TextField1"]').send_keys('Chavan')

driver.find_element(By.XPATH,'//input[@placeholder="Apartment, suite, etc. (optional)"]').send_keys('TestVagarant Technology')
driver.find_element(By.XPATH,'//*[@id="address1"]').send_keys('bangalore')
driver.implicitly_wait(2)
driver.find_element(By.XPATH,'//ul [@class="_3DmPe"]//*[@aria-label="Bangalore Railway Station Back Gate, M.G. Railway Colony, Majestic, Bengaluru, Karnataka, India"]').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//input[@id="save_shipping_information"]').click()

driver.find_element(By.XPATH,'//span[text()="Continue to shipping"]/parent::button').click()
driver.implicitly_wait()
driver.find_element(By.XPATH,'//span[text()="Continue to payment"]/parent::button').click()
driver.implicitly_wait()
driver.switch_to.frame(driver.find_element(By.XPATH,'(//iframe[@class="card-fields-iframe"])[1]'))
driver.find_element(By.XPATH,'//label[text()="Card number"]/following-sibling::input[@id="number"]').send_keys("1")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(By.XPATH,'(//iframe[@class="card-fields-iframe"])[2]'))
driver.find_element(By.XPATH,'//label[text()="Name on card"]/following-sibling::input[@id="name"]').send_keys("Sumit")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(By.XPATH,'(//iframe[@class="card-fields-iframe"])[3]'))
driver.find_element(By.XPATH,'//label[text()="Expiration date (MM / YY)"]/following-sibling::input[@id="expiry"]').send_keys("02/26")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(By.XPATH,'(//iframe[@class="card-fields-iframe"])[4]'))
driver.find_element(By.XPATH,'//label[text()="Security code"]/following-sibling::input[@id="verification_value"]').send_keys("123")
driver.switch_to.parent_frame();

driver.implicitly_wait(3)

driver.find_element(By.XPATH,'//span[text()="Pay now"]/parent::button').click()

driver.implicitly_wait(10)
driver.close()

















