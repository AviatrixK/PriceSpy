import requests
from bs4 import BeautifulSoup
import time
import random

# Provide your URL here
url = 'https://www.shopclues.com/mobiles-and-tablets.html?facet_brand%5b%5d=Apple&fsrc=facet_brand'

# Custom User-Agent to mimic a regular browser
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.59',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
]

file_name = "sw.html"

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

# Try to fetch the page content
def mainWebScraping():
    content = fetch_url(url)

    if content:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Create a new .html file and write the parsed content
        with open(f'{file_name}', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())  # You can use .prettify() for formatted HTML

        return(f"HTML content successfully saved as '{file_name}'")
    else:
        return("Failed to retrieve the page after several attempts.")

# Call the function to start scraping

# mainWebScraping()