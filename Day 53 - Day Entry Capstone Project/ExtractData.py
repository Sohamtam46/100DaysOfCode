import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"
LISTING_PRICES = []
LISTING_LINKS = []
LISTING_ADDRESSES = []

class ExtractData:
    def __init__(self):
        response = requests.get(URL)
        zillow_page_data = response.text
        soup = BeautifulSoup(zillow_page_data,"html.parser")
        class_name = "ListItem-c11n-8-84-3-StyledListCardWrapper"
        self.listings = soup.find_all(name="li",
                                      class_=class_name)

    def get_listing_price(self):
        for listing in self.listings:
            listing_price = listing.find(name="span",class_="PropertyCardWrapper__StyledPriceLine")
            LISTING_PRICES.append(listing_price.getText().strip("+/mo + 1 bd"))
        return LISTING_PRICES

    def get_listing_link(self):
        for listing in self.listings:
            listing_link = listing.find('a')
            LISTING_LINKS.append(listing_link.get('href'))
        return LISTING_LINKS

    def get_listing_address(self):
        for listing in self.listings:
            listing_address = listing.find('address')
            LISTING_ADDRESSES.append(listing_address.getText().replace(" |",",").strip())
        return LISTING_ADDRESSES