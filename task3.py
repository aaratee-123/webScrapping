from task1 import  scrape_top_list
from task2 import  scrape_top_list_1
import json 


screpped_data=scrape_top_list()
movie_by_year=scrape_top_list_1(screpped_data)
print(movie_by_year)
def group_by_decade(movie):
    movie_dec={}
    list1=[]
    for year in movie:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movie_dec[i]=[]
    for i in movie_dec:
        dec10=i+9
        for x in movie:
            if x<=dec10 and x>=i:
                for v in movie[x]:
                    movie_dec[i].append(v)
        with open("decade_year.json","w") as f:
            json.dump(movie_dec,f,indent=4)
    return (movie_dec)
print(group_by_decade(movie_by_year))


