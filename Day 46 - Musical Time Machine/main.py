import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

URL = "https://www.billboard.com/charts/hot-100"

# ===== IMP ======
# Generating browser.json
# In Firefox go onto YTMusic logged in and follow below instruction:
# Click the **Network** tab at the top of Developer Tools. In the Network tab's filter box, type `browse`. Refresh the page if you don't see any requests at all. Right click and Copy Value -> Copy Request Headers.
# In terminal type - ytmusicapi browser followed by pasting the above data copied from firefox and follow instructions on screen.
# ==================


# ---getting user date choice----
user_choice_date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD:")

# ---fetching site data for the given date----
response = requests.get(url=f"{URL}/{user_choice_date}")
billboard_site_data = response.text

# ---extracting all the song names of that days billboard list
soup = BeautifulSoup(billboard_site_data, "html.parser")
class_name = "c-title  a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max"
song_names = soup.find_all(name="h3",
                           class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
top_100_song_names = [song_name.getText().strip() for song_name in song_names]

# --- creating instance of ytmusic
yt = YTMusic("browser.json")

# ======== FIRST APPROACH ==========
# # search for all songs in billboard list
# song_video_ids = []
# for song_title in top_100_song_names:
#     try:
#         song_video_ids.append(yt.search(query=song_title,filter="songs",limit=1)[0]["videoId"])
#     except Exception as e:
#         print(e)
#
# # --- creating a playlist
# playlist_id = yt.create_playlist(
#     title=f"{user_choice_date} Billboard 100",
#     description=f"Billboard's top 100 songs on {user_choice_date}",
#     privacy_status="PRIVATE",
#     video_ids = song_video_ids
# )
# print(f"Created Playlist : {user_choice_date} Billboard 100")
# ======================================

# Create playlist
playlist_name = f"{user_choice_date} Billboard 100"
playlist_id = yt.create_playlist(
    playlist_name,
    f"Top songs from {user_choice_date}",
    privacy_status="PRIVATE",
)
print(f"Created playlist: {playlist_name}")

# Search and add each song
for song_title in top_100_song_names:
    try:
        search_results = yt.search(song_title, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song_title}")
    except Exception as e:
        print(f"Skipped: {song_title} | Reason: {e}")
