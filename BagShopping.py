from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testvagrant.myshopify.com/")
driver.find_element(by="xpath",value='//*[@id="Banner-template--16876710920493__image_banner"]/div[2]/div/div[2]/a').click()

driver.find_element(by="xpath",value='//*[@id="title-template--16876710854957__product-grid-8002225537325"]').click()

driver.find_element(by="xpath",value='//*[@id="product-form-template--16876710887725__main"]/div/div/div/div/div/button[1]').click()

driver.find_element(by="xpath",value='//*[@id="email"]').send_keys('sumitchavan5473@gmail.com')

driver.find_element(by="xpath",value='//*[@id="marketing_opt_in"]').click()

driver.find_element(by="xpath",value='//*[@id="TextField0"]').send_keys('Sumit')

driver.find_element(by="xpath",value='//*[@id="TextField1"]').send_keys('Chavan')

driver.find_element(by="xpath",value='//input[@placeholder="Apartment, suite, etc. (optional)"]').send_keys('TestVagarant Technology')
driver.find_element(by="xpath",value='//*[@id="address1"]').send_keys('bangalore')
sleep(3)
driver.find_element(by="xpath",value='//ul [@class="_3DmPe"]//*[@aria-label="Bangalore Railway Station Back Gate, M.G. Railway Colony, Majestic, Bengaluru, Karnataka, India"]').click()
sleep(3)
driver.find_element(by="xpath",value='//input[@id="save_shipping_information"]').click()

driver.find_element(by="xpath",value='//span[text()="Continue to shipping"]/parent::button').click()
sleep(2)
driver.find_element(by="xpath",value='//span[text()="Continue to payment"]/parent::button').click()
sleep(2)
driver.switch_to.frame(driver.find_element(by="xpath", value='(//iframe[@class="card-fields-iframe"])[1]'))
driver.find_element(by="xpath",value='//label[text()="Card number"]/following-sibling::input[@id="number"]').send_keys("1")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(by="xpath", value='(//iframe[@class="card-fields-iframe"])[2]'))
driver.find_element(by="xpath",value='//label[text()="Name on card"]/following-sibling::input[@id="name"]').send_keys("Sumit")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(by="xpath", value='(//iframe[@class="card-fields-iframe"])[3]'))
driver.find_element(by="xpath",value='//label[text()="Expiration date (MM / YY)"]/following-sibling::input[@id="expiry"]').send_keys("02/26")
driver.switch_to.parent_frame();

driver.switch_to.frame(driver.find_element(by="xpath", value='(//iframe[@class="card-fields-iframe"])[4]'))
driver.find_element(by="xpath",value='//label[text()="Security code"]/following-sibling::input[@id="verification_value"]').send_keys("123")
driver.switch_to.parent_frame();

sleep(3)

driver.find_element(by="xpath",value='//span[text()="Pay now"]/parent::button').click()

sleep(10)

















