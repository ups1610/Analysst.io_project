#=========usefull libraries==================

from bs4 import BeautifulSoup
import requests as r
import pandas as pd

#============links info===========================
u1 = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'
u2 = 'https://www.amazon.in/s?k=bags&page=2&crid=2M096C61O4MLT&qid=1675442806&sprefix=ba%2Caps%2C283&ref=sr_pg_2'
u3 = 'https://www.amazon.in/s?k=bags&page=3&crid=2M096C61O4MLT&qid=1675443757&sprefix=ba%2Caps%2C283&ref=sr_pg_2'
u4 = 'https://www.amazon.in/s?k=bags&page=4&crid=2M096C61O4MLT&qid=1675443946&sprefix=ba%2Caps%2C283&ref=sr_pg_3'
u5 = 'https://www.amazon.in/s?k=bags&page=5&crid=2M096C61O4MLT&qid=1675443971&sprefix=ba%2Caps%2C283&ref=sr_pg_5'
u6 = 'https://www.amazon.in/s?k=bags&page=6&crid=2M096C61O4MLT&qid=1675444038&sprefix=ba%2Caps%2C283&ref=sr_pg_6'
u7 = 'https://www.amazon.in/s?k=bags&page=7&crid=2M096C61O4MLT&qid=1675444325&sprefix=ba%2Caps%2C283&ref=sr_pg_7'
u8 = 'https://www.amazon.in/s?k=bags&page=8&crid=2M096C61O4MLT&qid=1675444156&sprefix=ba%2Caps%2C283&ref=sr_pg_8'
u9 = 'https://www.amazon.in/s?k=bags&page=9&crid=2M096C61O4MLT&qid=1675444162&sprefix=ba%2Caps%2C283&ref=sr_pg_9'
u10= 'https://www.amazon.in/s?k=bags&page=10&crid=2M096C61O4MLT&qid=1675444180&sprefix=ba%2Caps%2C283&ref=sr_pg_10'
u11= 'https://www.amazon.in/s?k=bags&page=11&crid=2M096C61O4MLT&qid=1675444355&sprefix=ba%2Caps%2C283&ref=sr_pg_11'
u12= 'https://www.amazon.in/s?k=bags&page=12&crid=2M096C61O4MLT&qid=1675444223&sprefix=ba%2Caps%2C283&ref=sr_pg_12'
u13= 'https://www.amazon.in/s?k=bags&page=13&crid=2M096C61O4MLT&qid=1675444379&sprefix=ba%2Caps%2C283&ref=sr_pg_13'
u14= 'https://www.amazon.in/s?k=bags&page=14&crid=2M096C61O4MLT&qid=1675444384&sprefix=ba%2Caps%2C283&ref=sr_pg_14'
u15= 'https://www.amazon.in/s?k=bags&page=15&crid=2M096C61O4MLT&qid=1675444400&sprefix=ba%2Caps%2C283&ref=sr_pg_15'
u16= 'https://www.amazon.in/s?k=bags&page=16&crid=2M096C61O4MLT&qid=1675444422&sprefix=ba%2Caps%2C283&ref=sr_pg_16'
u17= 'https://www.amazon.in/s?k=bags&page=17&crid=2M096C61O4MLT&qid=1675444439&sprefix=ba%2Caps%2C283&ref=sr_pg_17'
u18= 'https://www.amazon.in/s?k=bags&page=18&crid=2M096C61O4MLT&qid=1675444465&sprefix=ba%2Caps%2C283&ref=sr_pg_18'
u19= 'https://www.amazon.in/s?k=bags&page=19&crid=2M096C61O4MLT&qid=1675444493&sprefix=ba%2Caps%2C283&ref=sr_pg_19'
u20= 'https://www.amazon.in/s?k=bags&page=20&crid=2M096C61O4MLT&qid=1675444504&sprefix=ba%2Caps%2C283&ref=sr_pg_20'

url=[u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,u17,u18,u19,u20]
sheet=1
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

for u in url:
    # get response status
    page = r.get(u,headers=headers)# page response 200 ok

    #getting html data 
    soup = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup.prettify(),"html.parser").encode("utf-8")

    divs = soup.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")

    data = []

    for div in divs:
        #try to find the product url from the title div  classified to its class
        t_link = div.find("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
        link = t_link["href"] if t_link else 'NaN'

        #try to find the span element with the specified class
        span = div.find("span", class_="a-size-medium a-color-base a-text-normal")

        #if find get the text
        title = span.text if span else 'NaN'

        #try to find the span element with the specified class
        span = div.find("span",class_="a-size-base")
        # if find get the text
        rating = span.text if span else 'NaN'

        #try to find the span with the price class specified
        span = div.find("span",class_="a-price-whole")
        # if find get text
        price = span.text if span else "NaN"

        #try to find the reviews span from the classified class
        span = div.find("span", class_="a-size-base s-underline-text")
        # if find then get the text
        reviews = span.text if span else "NaN"

        data.append({
            'Product_Url':link,
            'Product_Name':title,
            'Price':price,
            'Rating':rating,
            'Review':reviews
        })
    #---Making dataframe 
    df = pd.DataFrame(data,columns=['Product_Url','Product_Name','Price','Rating','Review'])
    
    #---data in csv form
    df.to_csv(f"page{sheet}.csv",index=False,mode='w+')
    sheet=sheet+1



