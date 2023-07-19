import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the Excel file
df = pd.read_excel(r"C:\Users\diidhul\Desktop\ATA Fadhil\input.xlsx")
template_column = "Template"  # Column name containing the search queries


# Function to scrape the first search result from Google
def scrape_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all("div", {"class": "yuRUbf"})
    if search_results:
        first_result = search_results[1]
        link = first_result.find("a")["href"]
        return link
    return None


# Open the text file for writing
output_file = r"C:\Users\diidhul\Desktop\ATA Fadhil\output.txt"
with open(output_file, "w", encoding="utf-8") as file:
    # Iterate over the 'template' column and scrape the first search result for each query
    for query in df[template_column]:
        link = scrape_google(query)
        result = f"{query}, {link}"
        print(result)
        file.write(result + "\n")
