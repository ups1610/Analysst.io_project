#=========usefull libraries==================

from bs4 import BeautifulSoup
import requests as r

#============links info===========================
url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

# get response status
page = r.get(url,headers=headers)# page response 200 ok

soup = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup.prettify(),"html.parser").encode("utf-8")
print(soup2)
print("Succefully data get")

