from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



ACCOUNT_EMAIL = "soham.test@gmail.com"  # The email registered with
ACCOUNT_PASSWORD = "test@123"      # The password used during registration
GYM_URL = "https://appbrewery.github.io/gym/"



# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# create directory to store chrome profiles
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

