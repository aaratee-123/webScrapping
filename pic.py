import requests
from bs4 import BeautifulSoup
import json
import pprint

# pickle="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
# url_1=requests.get(pickle)
# soup=BeautifulSoup(url_1.text,"html.parser")

def pickle_in():
    pickle="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
    url_1=requests.get(pickle)
    soup=BeautifulSoup(url_1.text,"html.parser")
    # main_div=soup.find("div", class_="_1gx7")
    main_div=soup.find("div",class_="_3RA-")
    div=main_div.find_all("div",class_="UGUy")
    price=main_div.find_all("div",class_="_1kMS")


    i=0
    list1=[]
    Sr_no=0
    while i<len(div):
        Sr_no=Sr_no+1
        pickle_name=div[:24].get_text()
        pic_price=price[i].get_text()
        dic1={"Sr_no":Sr_no,"pickle_name":pickle_name,"price":pic_price}
        list1.append(dic1)
        with open("pickle_task.json","w") as f:
            json.dump(list1,f,indent=4)
        pprint.pprint(list1)
        i=i+1
pickle_in()




