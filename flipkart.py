import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

# scrapping data 
url="https://www.flipkart.com/search?q=mobiles"
req = requests.get(url)

soup=BeautifulSoup(req.content,"html.parser")

# i'm going to scrap titles

titles=soup.find_all('div',class_='_4rR01T')    # '_'is must in the class
# print(titles)



# now i'm going to scrap ratings

ratings=soup.find_all('div',class_='_3LWZlK')
# print(ratings)


#reviews

reviews=soup.find_all('span',class_='_2_R_DZ')
# print(reviews)


#prices


# prices=soup.find_all('div',class_='_25b18c')
# print(prices)



#storing scrap data in list

t_list = []
r_list = []
re_list = []

for title,rating,rev in zip(titles,ratings,reviews): #storing in zip file
    t_list.append(title.text)
    r_list.append(rating.text)
    re_list.append(rev.text)

# print(t_list)

#////////data saving in csv 

dict_data={'t_list':t_list, 'r_list':r_list, 're_list':re_list }
# print(dict_data)

#pandas
model=p.DataFrame(data=dict_data)

model.to_csv("mobilesdata.csv")



#  images

'''
img1=[]       # to append all image links in this list from j in for loop 
image=soup.findAll('div',class_="CXW8mj")     # it can find total data
# print(image)

for i in image:         # to get all image links
    j=i.img['src']
    #print(j)
    img1.append(j)
print(img1)'''

images=soup.find_all('div',class_='CXW8mj')
# print(images)

img=[]

for i in images:
    img.append(i)

print(img)