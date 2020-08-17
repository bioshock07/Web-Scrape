from bs4 import BeautifulSoup
import requests
import json,time


headers={'user_agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

url="https://www.amazon.in/Chromozome-Regular-T-Shirt-OS-10_White-Grey_L/dp/B07CQMYL95"

resp=requests.get(url,headers=headers)
s=BeautifulSoup(resp.content,features="lxml")
time.sleep(3)
#product_title=s.select("#productTitle")[0].get_text().strip() 
#print(product_title)
#product_price=s.select("#priceblock_ourprice")[0].get_text()
#print(product_price)
#product_stars=s.select("#acrPopover")[0].get_text()
#print(product_stars)
#product_rating=s.select("#acrCustomerReviewText")[0].get_text()
#print(product_rating)

dictionary={
	"product_title" : s.select("#productTitle")[0].get_text().strip(), 
	"product_price" : s.select("#priceblock_ourprice")[0].get_text(),		
	"product_stars" : s.select("#acrPopover")[0].get_text(),
	"product_rating" : s.select("#acrCustomerReviewText")[0].get_text(),
}
with open("amazon.json","w")as outfile:
	json.dump(dictionary,outfile)
	print("Json Created")

