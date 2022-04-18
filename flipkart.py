import re
from bs4 import BeautifulSoup
import requests

def url_list_for_flipkart(input_text):
    link_list = list()
    while True:
        temp_list = list()
        img_link = ""
        link=""
        price = ""
        try:
            index_img = input_text.index('"media"') + input_text[input_text.index('"media"'):].index("http://")
            index_link = input_text.index('"baseUrl":"') + 11
            index_price = input_text.index('"finalPrice":{"a') + 69
        except:
            break
        while True:
            img_link += input_text[index_img]
            index_img +=1
            if ".jpeg?" in img_link:
                img_link = img_link.replace("{@width}","500")[:-1]
                img_link = img_link.replace("{@height}","1000")
                temp_list.append(img_link)
                break
        while True:
            link += input_text[index_link]
            index_link +=1
            if "," in link:
                link = link[:-2]
                temp_list.append("https://www.flipkart.com"+link)
                temp_list.append(link[1:link[1:].index("/")+1].replace("-"," ").title())
                break
        while True:
            price += input_text[index_price]
            index_price += 1
            if "," in price:
                price = price[:-2]
                temp_list.append("Rs. "+price)
                break
        input_text = input_text.replace('"media"', "", 1)
        input_text = input_text.replace('"baseUrl":"', "", 1)
        input_text = input_text.replace('"finalPrice":{"a', "", 1)
        link_list.append(temp_list)
    return link_list


def flipkart(searches):
    result = list()
    for search in searches:
        headers = {"User-Agent": "Edge/90.0.818.46"}
        source = requests.get("https://www.flipkart.com/search?q="+search,headers=headers).text
        soup = BeautifulSoup(source,"html.parser").prettify()
        for i in url_list_for_flipkart(str(soup)):
            result.append(i)
    return result

print(flipkart(["watches"]))
