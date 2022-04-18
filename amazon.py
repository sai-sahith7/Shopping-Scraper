import re
from bs4 import BeautifulSoup
import requests

def amazon(searches):
    result = list()
    for search in searches:
        headers = {"User-Agent": "Defined"}
        while True:
            source = requests.get("https://www.amazon.in/s?k="+search,headers=headers).text
            soup = BeautifulSoup(source,"html.parser").prettify()
            if "It's rush hour and traffic is piling up on that page. Please try again in a short while." not in str(soup):
                break
        soup2 = BeautifulSoup(soup,"html.parser")
        parent_tag = soup2.find_all("div", attrs={"data-component-type" : "s-search-result"})
        price = list();link = list();image = list();title = list()
        for tag in parent_tag:
            try:
                price.append(tag.findChild("span", attrs={"class" : "a-price-whole"}).text.strip())
                link.append(tag.findChild("a", attrs={"class" : "a-link-normal s-no-outline"})["href"])
                image.append(tag.findChild("img", attrs={"class" : "s-image" })["src"])
                title.append(tag.findChild("img", attrs={"class" : "s-image" })["alt"])
            except:
                continue
        for i in range(len(link)):
            result.append([image[i],"https://www.amazon.in"+link[i],title[i],"Rs. "+price[i]])
    return result

print(amazon(["iphone"]))
