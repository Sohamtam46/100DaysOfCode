from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os


ACCOUNT_EMAIL = "soham.test@gmail.com"  # The email registered with
ACCOUNT_PASSWORD = "test@123"      # The password used during registration
GYM_URL = "https://appbrewery.github.io/gym/"
CLASS_BOOKED = "Booked"
CLASS_JOIN_WAITLIST = "Join Waitlist"
CLASS_ON_WAITLIST = "Waitlisted"
CLASS_AVAILABLE = "Book Class"
NUM_CLASS_BOOKED : int = 0
WAITLIST_JOINED : int = 0
CLASS_ALREADY_BOOKED : int = 0
DETAILED_CLASS_LIST = ""





# To keep the window from shutting down we enable this option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
# create directory to store chrome profiles
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)


# logging into the site
wait = WebDriverWait(driver, timeout=10)

login = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login.click()

# logging in
email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.send_keys(ACCOUNT_EMAIL)
pass_input = driver.find_element(By.ID,value="password-input")
pass_input.send_keys(ACCOUNT_PASSWORD)
# hit submit
submit_btn = driver.find_element(By.ID,value="submit-button")
submit_btn.click()

# wait until schedule page loads
schedule_page = wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# find the gym cards for next tuesday
# tuesday_cards = driver.find_element(By.CSS_SELECTOR,"div[id*='tue']")
# class_day_title = tuesday_cards.find_element(By.CSS_SELECTOR,"h2[id^='day-title-']").text
# user_choice_class = tuesday_cards.find_element(By.CSS_SELECTOR,"div[id*='-1800']")
# class_button = user_choice_class.find_element(By.TAG_NAME,"button")
# class_name = user_choice_class.find_element(By.CSS_SELECTOR,"h3[id^='class-name-']").text
# class_time = user_choice_class.find_element(By.CSS_SELECTOR,"p[id^='class-time-']").text
class_cards = driver.find_elements(By.CSS_SELECTOR,"div[id^='day-group-']")
for class_card in class_cards:
    if "tue" in class_card.get_attribute("id") or "thu" in class_card.get_attribute("id"):
        class_day_title = class_card.find_element(By.CSS_SELECTOR,"h2[id^='day-title-']").text
        user_choice_class = class_card.find_element(By.CSS_SELECTOR,"div[id*='-1800']")
        class_button = user_choice_class.find_element(By.TAG_NAME,"button")
        class_name = user_choice_class.find_element(By.CSS_SELECTOR,"h3[id^='class-name-']").text
        class_time = user_choice_class.find_element(By.CSS_SELECTOR,"p[id^='class-time-']").text
        class_status = user_choice_class.find_element(By.CSS_SELECTOR,"button[id^='book-button-']").text
        if class_status == CLASS_AVAILABLE:
            NUM_CLASS_BOOKED += 1
            class_button.click()
            print(f"✓ Booked: {class_name} on {class_day_title} at {class_time}!")
            DETAILED_CLASS_LIST += f"• [New Booking] {class_name} on {class_day_title} at {class_time}!\n"
        elif class_status == CLASS_JOIN_WAITLIST:
            WAITLIST_JOINED += 1
            class_button.click()
            print(f"✓ Joined Waitlist: {class_name} on {class_day_title} at {class_time}!")
            DETAILED_CLASS_LIST += f"• [New Waitlist] {class_name} on {class_day_title} at {class_time}!\n"
        elif class_status == CLASS_BOOKED:
            CLASS_ALREADY_BOOKED += 1
            print(f"{class_name} on {class_day_title} at {class_time} already Booked!")
        elif class_status == CLASS_ON_WAITLIST:
            CLASS_ALREADY_BOOKED += 1
            print(f"Already on waitlist!")
print("\n")
# printing summary
print(
    f"--- BOOKING SUMMARY ---\n"
    f"Classes booked: {NUM_CLASS_BOOKED}\n"
    f"Waitlists joined: {WAITLIST_JOINED}\n"
    f"Already booked/waitlisted: {CLASS_ALREADY_BOOKED}\n"
    f"Total Tuesday & Thursday 6pm classes: {NUM_CLASS_BOOKED + WAITLIST_JOINED + CLASS_ALREADY_BOOKED}"
    f"\n"
    )
print(
    f"--- DETAILED CLASS LIST ---\n"
    f"{DETAILED_CLASS_LIST}"
)