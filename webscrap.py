# Step 1: Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

#  Fetch the website
#website2

url = "https://webscraper.io/test-sites/e-commerce/static"
response = requests.get(url)

# Parse the content
soup = BeautifulSoup(response.content, "html.parser")

# Extract product prices
prices = soup.find_all("span", {"itemprop": "price"})
WEb1products = []

if response.status_code == 200:
    for data in prices:
        price = data.get_text().strip().replace("$", "")
        try:
            price_float = float(price.replace(",", ""))  # convert to float
            WEb1products.append(price_float)
        except:
            continue


    # Create DataFrame
    
    df = pd.DataFrame({
        'WEb1products': WEb1products
    })

    # Calculate average price
    '''
    avg_price = df['WEb1products'].mean()
    print("webscraper test site average price:", avg_price)
    '''
    
else:
    print("Failed to fetch the page, status code:", response.status_code)

print(df)    

#website 2
response = requests.get('https://books.toscrape.com/')

#  Parse the content

soup = BeautifulSoup(response.content ,'html.parser')

#  Check the response and fetch content


prize = soup.find_all('article',class_="product_pod")
products = []

if response.status_code == 200:
  for data in prize:
    title = data.h3.a['title']
    price = data.find('p',class_='price_color').text
    
    price_str = price.strip().replace("£",'')
    price_strs = float(price_str)
    
    products.append(price_strs)
# making the dataframe 
    df = pd.DataFrame({
  'products':products
   })

print(df)


# --- Data ---
web1 = pd.DataFrame({"products": [1799.00, 1178.99, 416.99]})
toscrap = pd.DataFrame({
    "products": [51.77, 53.74, 50.10, 47.82, 54.23, 22.65, 33.34, 17.93, 22.60, 
                 52.15, 13.99, 20.66, 17.46, 52.29, 35.02, 57.25, 23.88, 37.59, 
                 51.33, 45.17]
})



# --- Calculate averages ---
web1_mean = web1["products"].mean()
toscrap_mean = toscrap["products"].mean()

# Create summary dataframe
summary = pd.DataFrame({
    "Website": ["Webscraper Test Site", "Toscrap Site"],
    "Average Price": [web1_mean, toscrap_mean]
})
#saving data to csv
summary.to_csv("output_csv",index=False)

# --- Bar Chart ---
plt.figure(figsize=(4,3))
plt.bar(summary["Website"], summary["Average Price"], color=["skyblue","lightgreen"])
plt.title("Average Price Comparison")
plt.ylabel("Average Price")
plt.show()

# --- Pie Chart ---
plt.figure(figsize=(4,4))
plt.pie(summary["Average Price"], labels=summary["Website"], autopct="%.1f%%", 
        startangle=90, colors=["skyblue","lightgreen"])
plt.title("Share of Average Prices by Website")
plt.show()