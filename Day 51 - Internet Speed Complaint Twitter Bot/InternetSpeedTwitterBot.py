from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import random

SPEEDTEST_URL = "https://www.speedtest.net/"



class InternetSpeedTwitterBot:
    def __init__(self,up,down):
        # To keep the window from shutting down we enable this option
        chrome_options = uc.ChromeOptions()
        # chrome_options.add_argument(
            # "--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(chrome_options,keep_alive=True)
        self.wait = WebDriverWait(self.driver, timeout=10)


    def get_internet_speed(self):
        # fetched the current up/down speed from speedtest.net
        self.driver.get(SPEEDTEST_URL)
        privacy_notice_button = self.wait.until(ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        privacy_notice_button.click()

        go_button = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "start-text")))
        go_button.click()

        download_speed = self.driver.find_element(By.CLASS_NAME,"download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME,"upload-speed")
        # wait till speeds came up for both upload and download
        while download_speed.get_attribute("data-download-status-value") == "NaN":
            pass
        down_speed = download_speed.text
        while upload_speed.get_attribute("data-upload-status-value") == "NaN":
            pass
        up_speed = upload_speed.text

        return down_speed,up_speed


    def tweet_at_provider(self,email,password):
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(3)

        def human_type(input_element, text, min_delay=0.05, max_delay=0.15):
            """Function to type with random delays per character to make it more human-like."""

            for char in text:
                input_element.send_keys(char)
                time.sleep(random.uniform(min_delay, max_delay))


        username_input = self.wait.until(ec.element_to_be_clickable((By.NAME,"text")))
        human_type(input_element=username_input,text=email)

        time.sleep(2)
        username_input.send_keys(Keys.ENTER)

        password_input = self.wait.until(ec.element_to_be_clickable((By.NAME,"password")))
        password_input.send_keys(password)

        # to keep the window open
        input("Press Enter to close the browser...")
