import requests
from bs4 import BeautifulSoup

# Use of yellowpages.com information is strictly for academic purposes, and there is no claim to the data or
# information with the intent of ownership.
url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=San+Jose%2C+CA"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print(item.contents[0].find_all("a", {"class": "business-name"})[0].text)
    try:
        print(item.contents[1].find_all("span", {"class": "street-address"})[0].text.replace(",", ""))
    except:
        pass
    try:
        print(item.contents[1].find_all("span", {"class": "locality"})[0].text.replace(",", ""))
    except:
        pass
    try:
        print(item.contents[1].find_all("span")[3].text)
    except:
        pass
    try:
        print(item.contents[1].find_all("span")[4].text)
    except:
        pass
    finally:
        print(" ")


# print(soup.prettify())


# for link in soup.find_all()

