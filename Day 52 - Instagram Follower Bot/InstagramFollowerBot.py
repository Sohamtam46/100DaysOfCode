from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import random
import os

from websockets.utils import accept_key

INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_EMAIL = os.getenv("INSTAGRAM_EMAIL")
INSTAGRAM_PASS = os.getenv("instagram_pass")

class InstagramFollowerBot:

    def __init__(self):
        # To keep the window from shutting down we enable this option
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled")  # Prevents Chrome from detecting Selenium controlling it.
        chrome_options.add_argument("--no-first-run")  # Stops Chrome from opening up profile page on startup.
        chrome_options.add_argument(
            "--no-default-browser-check")  # Stops Chrome from asking about making it default browser
        self.driver = uc.Chrome(chrome_options, keep_alive=True)
        # self.wait = WebDriverWait(self.driver, timeout=10)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(4)


        accept_cookies = self.driver.find_element(By.CLASS_NAME, '_asz1')
        accept_cookies.click()

        def human_type(input_element, text, min_delay=0.05, max_delay=0.15):
            """Function to type with random delays per character to make it more human-like."""

            for char in text:
                input_element.send_keys(char)
                time.sleep(random.uniform(min_delay, max_delay))

        time.sleep(2)
        username_input = self.driver.find_element(By.NAME,"email")
        human_type(input_element=username_input,text=INSTAGRAM_EMAIL)

        time.sleep(2)
        password_input = self.driver.find_element(By.NAME, "pass")
        human_type(input_element=password_input, text=INSTAGRAM_PASS)

        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(10)
        save_info_popup = self.driver.find_element(By.CLASS_NAME,'x1e56ztr')
        save_info_popup.click()

        time.sleep(4)
        notification_popup = self.driver.find_element(By.CLASS_NAME,'_a9_1')
        notification_popup.click()

        time.sleep(2)
        self.driver.get(f"{INSTAGRAM_URL}rockstargames/")

        # time.sleep(3)
        # following_count = self.driver.find_element(By.XPATH, "//a[@role='link'][contains(., 'following')//span[contains(@class, 'x1s688f')]")
        # print(f"followers = {following_count.text}")
        time.sleep(2)
        followings_button = self.driver.find_element(by=By.XPATH, value="//span[contains(text(), ' following')]")
        followings_button.click()



    def find_followers(self):

        time.sleep(3)
        modal_xpath = "/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        try:
            # scr1 = self.driver.find_element(By.CSS_SELECTOR,'.x6nl9eh.x1a5l9x9.x7vuprf')
            scr1 = self.driver.find_element(By.XPATH,modal_xpath)
            for i in range(20):
                print("Scrolling..")
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                time.sleep(random.uniform(2,3))
        except NoSuchElementException:
            print("No Scrollable Element Found!")
        # to keep the window open
        input("Press Enter to close the browser...")