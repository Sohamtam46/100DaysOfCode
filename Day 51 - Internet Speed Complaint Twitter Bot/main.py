from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import os

# --- Constants ---
PROMISED_DOWN = 200
PROMISED_UP = 100
TWITTER_EMAIL = os.environ.get("X_USERNAME")
TWITTER_PASS = os.environ.get("X_PASS")

InternetSpeedTwitterBot = InternetSpeedTwitterBot(PROMISED_UP,PROMISED_DOWN)

# current_down,current_up = InternetSpeedTwitterBot.get_internet_speed()
#
#
# print(f"Current Upload Speed = {current_up} Mbps")
# print(f"Current Download Speed = {current_down} Mbps")
#
# if int(current_up) < PROMISED_UP or int(current_down) < PROMISED_DOWN:
#     InternetSpeedTwitterBot.tweet_at_provider(TWITTER_EMAIL,TWITTER_PASS)
InternetSpeedTwitterBot.tweet_at_provider(TWITTER_EMAIL,TWITTER_PASS)