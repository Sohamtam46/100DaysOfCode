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

# accept cookies
time.sleep(1)
cookie_accept_btn = driver.find_element(By.CLASS_NAME, value="cc_btn_accept_all")
cookie_accept_btn.click()

time.sleep(1) # wait till cookie appears on screen
# finding the cookie button element
cookie_button = driver.find_element(By.ID,value="bigCookie")

def upgrade_product():
    # check the most expensive products available and buy it
    print("upgrade product")
    products = driver.find_element(By.ID, value="products")
    # while True:
    #     unlocked_products = products.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    #     if len(unlocked_products) > 0:
    #         unlocked_products[-1].click()
    #     else:
    #         break
    unlocked_products = products.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    if len(unlocked_products) > 0:
        unlocked_products[-1].click()


def upgrade_upgrades():
    # check all available upgrades and buy it
    print("upgrade upgrades")
    upgrades = driver.find_element(By.ID, value="upgrades")
    upgrades_unlocked = upgrades.find_elements(By.CSS_SELECTOR, value=".crate.upgrade.enabled")
    if len(upgrades_unlocked) > 0:
        for each_upgrade in upgrades_unlocked:
            each_upgrade.click()



# time.time() gives the current time since epoch
# The epoch is the point where the time starts, the return value of time.gmtime(0).
# It is January 1, 1970, 00:00:00 (UTC) on all platforms.

timeout = time.time() + 60*TIMEOUT_MINUTE # to stop the bot after given min
upgrade_check_time = time.time() + 5 # check upgrade every 5 sec

COUNT = 0

while timeout > time.time():
    cookie_button.click()
    if time.time() > upgrade_check_time:
        if COUNT % 2 == 0:
            upgrade_product()
            COUNT += 1
        else:
            upgrade_upgrades()
            COUNT += 1
        upgrade_check_time = time.time() + 5.0

cookie_per_second = driver.find_element(By.ID, value="cookies")
print(f"Cookie {cookie_per_second.text}")

