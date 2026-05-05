from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TIMEOUT_MINUTE = 5

# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# language selection
time.sleep(1) # till the page loads the language selection menu
language_selection = driver.find_element(By.CLASS_NAME, value="langSelectButton")
language_selection.click()

time.sleep(1) # wait till cookie appears on screen
# finding the cookie button element
cookie_button = driver.find_element(By.ID,value="bigCookie")

# time.time() gives the current time since epoch
# The epoch is the point where the time starts, the return value of time.gmtime(0).
# It is January 1, 1970, 00:00:00 (UTC) on all platforms.

timeout = time.time() + 60*TIMEOUT_MINUTE # to stop the bot after given min
upgrade_check_time =

while timeout > time.time():
    cookie_button.click()


