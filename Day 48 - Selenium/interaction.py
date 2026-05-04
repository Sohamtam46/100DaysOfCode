from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

# navigating to the page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # Using XPATH to get hold of an element
# article_figure = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_figure.click()

# # Using Link Text to get hold of element
# wikiversity = driver.find_element(By.LINK_TEXT, value="Wikiversity")
# wikiversity.click()

search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_icon.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
