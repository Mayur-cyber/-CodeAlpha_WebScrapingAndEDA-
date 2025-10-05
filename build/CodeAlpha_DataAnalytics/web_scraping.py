import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract book details
books = soup.find_all("article", class_="product_pod")
data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    data.append([title, price, availability])

# Save to CSV
df = pd.DataFrame(data, columns=["Title", "Price", "Availability"])
df.to_csv("books_data.csv", index=False)

print("Data scraped & saved to books_data.csv")
