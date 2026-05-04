from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_figure = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_figure.text)