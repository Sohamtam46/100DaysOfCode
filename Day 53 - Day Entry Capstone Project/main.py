from ExtractData import ExtractData
from FormFilling import FormFilling

ExtractData = ExtractData()
FormFilling = FormFilling()

listing_prices = ExtractData.get_listing_price()
listing_links = ExtractData.get_listing_link()
listing_addresses = ExtractData.get_listing_address()

for i in range(len(listing_addresses)):
    FormFilling.upload_data(address=listing_addresses[i],price=listing_prices[i],link=listing_links[i])