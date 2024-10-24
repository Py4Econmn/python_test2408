import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract data from each page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the table
    table = soup.find('table')
    rows = table.find_all('tr')
    
    # Collect table data
    table_data = []
    for row in rows[1:]:  # Skip header row
        cols = row.find_all('td')
        table_data.append([col.text.strip() for col in cols])

    # Extract the content from p[2] and p[3]/text()
    p2 = soup.select_one('body > p:nth-of-type(2)').text.strip()
    p3_text = soup.select_one('body > p:nth-of-type(3)').text.strip()

    return table_data, p2, p3_text

# Initialize lists to store the data
all_table_data = []
page_identifiers = []

# Iterate over the 240 pages
for i in range(1, 25):  # First range
    for j in range(1, 11):  # Second range
        url = f"http://list.eec.mn/{i}/{j}.html?"
        print(f"Scraping {url}...")
        
        try:
            table_data, p2, p3_text = scrape_page(url)
            all_table_data.extend(table_data)
            
            # Add page identifiers for each row of the table
            page_identifiers.extend([(p2, p3_text)] * len(table_data))
        except Exception as e:
            print(f"Error scraping {url}: {e}")

# Convert the data into a DataFrame
columns = ['Байр', 'Бүртгэлийн дугаар', 'А.Оноо', 'Х.Оноо', 'Про', 'А.Ч.И', 'Page Identifier 1', 'Page Identifier 2']
df = pd.DataFrame([row + list(page_id) for row, page_id in zip(all_table_data, page_identifiers)], columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False)
print("Data saved to scraped_data.csv")

df = pd.read_csv('scraped_data.csv')
def clean_text(text):
    parts = text.split(':')
    if len(parts) > 1:
        return parts[1].strip()  # Get the part after the period and remove leading spaces
    return text.strip()

df.columns

df['Page Identifier 2'] = df['Page Identifier 2'].apply(clean_text)
df['Аймаг'] = df['Аймаг'].apply(clean_text)

cols = list(df.columns)
cols[-2:] = ['Аймаг','Хичээл']
df.columns = cols

df.to_csv('scraped_data.csv', encoding='utf-8-sig',index=False)