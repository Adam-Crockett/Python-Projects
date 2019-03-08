import requests
from bs4 import BeautifulSoup
# Use of practicepython.org practice files are strictly for academic use.


url = "http://www.practicepython.org/assets/Training_01.txt"
r = requests.get(url)
soup = BeautifulSoup(r.content)
# data = soup.find_all("p")
with open("training_01", "w") as open_file:
    for item in soup:
        try:
            open_file.write(str(soup))
        except:
            pass

