import requests
from bs4 import BeautifulSoup
import time
import random
import json

# Provide your URL here
# url = 'https://www.shopclues.com/search?q=watches'
# url = 'https://www.shopclues.com/appliances-air-conditioners.html'
# url = 'https://www.shopclues.com/mobiles-and-tablets.html?facet_brand%5b%5d=Apple&fsrc=facet_brand'
# url = 'https://www.snapdeal.com/search?clickSrc=top_searches&keyword=saree&sort=rlvncy'
# ❤️url = 'https://www.flipkart.com/sarees-store'
# Custom User-Agent to mimic a regular browser
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.59',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
]

file_name = "sw_2.html"

# Function to handle retries
def fetch_url(url, retries=5, delay=5):
    for attempt in range(retries):
        headers = {
            'User-Agent': random.choice(user_agents),  # Randomly select a user agent
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.content
        elif response.status_code == 503:
            print(f"503 Service Unavailable. Retrying... Attempt {attempt + 1}/{retries}")
            time.sleep(delay)
            delay += random.randint(1, 3)  # Increase delay with each attempt
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            break
    return None

def extractShopclues(soup) :
    prod_div = soup.find_all("div",class_ = 'col3')
    # print(prod_div)
    prod_list=[]
    for div in prod_div:
        # print(div)
        all_info={}
        imgTag = div.find("img")
        if imgTag.get("src") and imgTag:
            all_info["img"]=imgTag["src"]
            all_info["name"]=imgTag["title"]
        priceTag = div.find("span",class_ = 'p_price')
        if priceTag:
            all_info['price']=priceTag.text.strip()
        old_price = div.find("span",class_ = 'old_prices')
        if old_price:
            old_price1 = old_price.find("span")
            if old_price1:
                all_info["old_price"]=old_price1.text.strip()
        discount = div.find("span",class_ = 'prd_discount')
        if discount:
            all_info["discount"]=discount.text.strip()

        if all_info:
            prod_list.append(all_info)
    jsondata = json.dumps(prod_list,indent=4)
    # print(prod_list)
    return jsondata 




def extractSnapdeal(soup):    
    prod_div = soup.find_all("div",class_ = 'product-tuple-listing')
    # print(prod_div)
    prod_list =  []
    for div in prod_div:
        all_info = {}
        imgTag = div.find("img")
        if imgTag.get("src") and imgTag:
            all_info["img"]=imgTag["src"]
            all_info["name"]=imgTag["title"]
            priceTag = div.find("div",class_ = 'product-price-row')
            if priceTag:
                prod_price = priceTag.find("span", class_ = 'product-price')
                all_info['price']=prod_price.text.strip()
                old_price = priceTag.find("span",class_ = 'lfloat product-desc-price strike')
                if old_price:
                    all_info["old_price"]=old_price.text.strip()
                discount = priceTag.find("div",class_ = 'product-discount')
                if discount:
                    discount1 = discount.find("span")
                    all_info["discount"]=discount1.text.strip()
        if all_info:
            prod_list.append(all_info)
            print(all_info)
    jsondata = json.dumps(prod_list,indent=4)
    return jsondata


def writefile(data,filename):
    file_name = filename
    with open(f"{file_name}", 'a', encoding='utf-8') as file:
        file.write(data)
    

# Try to fetch the page content
def mainWebScraping(name):
    urls = {}
    urls['shopClues'] = (f'https://www.shopclues.com/search?q={name}')
    urls['snapDeal'] = (f'https://www.snapdeal.com/search?clickSrc=top_searches&keyword={name}&sort=rlvncy')
    # print(urls)
    falsify = False
    for url in urls:
        print(url)
        content = fetch_url(urls[url])
        # print(content)
        if content:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')
            if url =="snapDeal":
                p_data = extractSnapdeal(soup)
            elif url == "shopClues":
                p_data = extractShopclues(soup)

            # Create a new .html file and write the parsed content
            with open(f'{file_name}', 'w', encoding='utf-8') as file:
                file.write(soup.prettify())  # You can use .prettify() for formatted HTML
            writefile(p_data,"product_data1")
            # writefile(snapDeal,"product_data1")
            # return(f"HTML content successfully saved as '{file_name}'")
            falsify = True
        else:
            # print("Failed to retrieve the page after several attempts.")
            falsify = False
            continue
    if falsify :
        return(f"HTML content successfully saved as '{file_name}'")
    else:
        return("Failed to retrieve the page after several attempts.")

# Call the function to start scraping

# mainWebScraping('saree')

