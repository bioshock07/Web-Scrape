from bs4 import BeautifulSoup
import requests
import json,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def close_last_tab():
    if (len(driver.window_handles) == 2):
        driver.switch_to.window(window_name=driver.window_handles[0])
        driver.close()
        driver.switch_to.window(window_name=driver.window_handles[-1])

headers={'user_agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


options = webdriver.ChromeOptions()
options.binary_location = "C:\\Users\\lenovo pc\\AppData\\Local\\GoogleChromeApplication\\chrome.exe"
chrome_driver_binary = "C:\\Users\\lenovo pc\\Documents\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
time.sleep(3)
driver.get('https://www.amazon.in/')
driver.maximize_window()
wait = ui.WebDriverWait(driver,3)
wait.until(page_is_loaded)


SearchBar=driver.find_element_by_id("twotabsearchtextbox")
SearchBar.clear()
SearchBar.send_keys('t-shirt', Keys.ARROW_DOWN)
SearchBar.send_keys(Keys.RETURN)
time.sleep(2)


product = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located(
    (By.CLASS_NAME,'s-image')))
print(product[1].text)
product[1].click()
sleep(2)
close_last_tab()
sleep(2)
url= driver.current_url
print(url)
sleep(2)
resp=requests.get(url,headers=headers)
s=BeautifulSoup(resp.content,features="lxml")
time.sleep(1)

print("printing beautifulSoup:", s)
dictionary={
	"product_title" : s.select("#productTitle")[0].get_text().strip(),
	"product_price" : s.select("#priceblock_ourprice")[0].get_text(),
	"product_stars" : s.select("#acrPopover")[0].get_text(),
	"product_rating" : s.select("#acrCustomerReviewText")[0].get_text(),
}
with open("amazon1.json","w")as outfile:
    json.dump(dictionary,outfile)
    print("Json Created")
driver.quit()