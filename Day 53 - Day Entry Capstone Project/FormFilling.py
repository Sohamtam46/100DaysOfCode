from selenium import webdriver
from selenium.webdriver.common.by import By
import time

RESEARCH_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfR4zw3bypsGOf_Vh7ngg-lV1dPfbpSDkgk57KGjPPR1tLzjA/viewform?usp=publish-editor"

class FormFilling:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(RESEARCH_FORM)

    def upload_data(self,address,price,link):
        time.sleep(2)
        data = [address,price,link]
        answer_inputs = self.driver.find_elements(By.CLASS_NAME,"Qr7Oae")
        for i,input in enumerate(answer_inputs):
            input_space = input.find_element(By.TAG_NAME,"input")
            input_space.send_keys(data[i])
        submit_button = self.driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Submit')]")
        submit_button.click()

        time.sleep(2)
        submit_another_res = self.driver.find_element(By.TAG_NAME,"a")
        submit_another_res.click()

