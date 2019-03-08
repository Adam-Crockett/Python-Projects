import requests
from bs4 import BeautifulSoup

# Use of vanityfair.com information is strictly for academic purposes, and there is no claim to the data or
# information with the intent of ownership.
url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)

soup = BeautifulSoup(r.content)
g_data = soup.find_all("p")

for item in g_data:
    try:
        print(item.contents[0])
    except:
        pass


