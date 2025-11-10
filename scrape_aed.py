import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Webpage URL
url = "https://www.aedportugal.pt/en/members/"

# 2. Download the page
response = requests.get(url)
response.raise_for_status()  # Stop if page fails
html_content = response.text

# 3. Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# 4. Find all company blocks
members = soup.find_all("div", class_="et_pb_team_member_description")

# 5. Extract company names and websites
company_names = []
company_websites = []

for member in members:
    # Company name
    name_tag = member.find("h4")
    if name_tag:
        company_names.append(name_tag.get_text(strip=True))
    else:
        company_names.append("N/A")
    
    # Website
    link_tag = member.find("a", href=True)
    if link_tag:
        company_websites.append(link_tag['href'])
    else:
        company_websites.append("N/A")

# 6. Save to Excel
df = pd.DataFrame({
    "Company Name": company_names,
    "Website": company_websites
})

df.to_excel("aed_portugal_companies.xlsx", index=False)
print("File saved as 'aed_portugal_companies.xlsx'")
