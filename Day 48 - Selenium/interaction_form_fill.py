from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

# navigating to the page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# entering details
fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Test")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("lname_test")
email = driver.find_element(By.NAME, value="email")
email.send_keys("test@test.com")

sign_up_btn = driver.find_element(By.TAG_NAME,value="button")
sign_up_btn.click()

