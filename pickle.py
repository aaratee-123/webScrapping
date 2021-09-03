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
    pickle_link=main_div.find_all("div",class_="_3WhJ")


    i=0
    list1=[]
    Sr_no=0
    while i<len(pickle_link):
        Sr_no=Sr_no+1
        # pickle_name=pickle_link[i].get_text()
        pickle_name=div[i].get_text()
        # pic_name=pickle_name[i]
        # wt=pickle_name[i]

        # print(pickle_name)
        pic_price=price[i].get_text()
        pickle_url1=pickle_link[i].a['href']
        # name=pickle_name[0:24]
        # gram=pickle_name[21:26]
        pic_url2="https://paytmmall.com/"+pickle_url1
        dic1={"Sr_no":Sr_no,"pic_name":pickle_name,"pickle_url1":pic_url2,"price":pic_price}
        list1.append(dic1)
        with open("pic_task.json","w") as f:
            json.dump(list1,f,indent=4)
        pprint.pprint(list1)
        i=i+1
pickle_in()




