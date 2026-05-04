from selenium import webdriver
from selenium.webdriver.common.by import By


# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.co.uk/Amazfit-Direction-Fitness-Resistant-Silicone/dp/B0DSPWKJW4/ref=sr_1_5?sr=8-5")
#
# price_euro = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The Price is : {price_euro.text}.{price_cents.text}")

driver.get("https://www.python.org/")

latest_events = {}

event_list = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li')
for i,event in enumerate(event_list):
    event_date = event.text.split("\n")[0]
    event_name = event.text.split("\n")[1]
    latest_events[i] = {
        "time": event_date,
        "name": event_name
    }


print(latest_events)


# driver.close() #close the tab
driver.quit() #close the browser
