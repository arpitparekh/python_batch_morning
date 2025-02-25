import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.geeksforgeeks.org/jdk-in-java/"

# Send an HTTP GET request
# headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url)

print(response.text)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the title of the article
    title = soup.find("h1").text.strip()
    print(f"Title: {title}")

    # Extract all paragraphs
    paragraphs = soup.find_all("p")
    for idx, para in enumerate(paragraphs, start=1):
        print(f"\nParagraph {idx}: {para.text.strip()}")

    # Extract all headings (h2, h3, etc.)
    headings = soup.find_all(["h2", "h3"])
    for head in headings:
        print(f"\nHeading: {head.text.strip()}")

    # Extract all links
    links = soup.find_all("a", href=True)
    for link in links[:10]:  # Print only first 10 links
        print(f"Link: {link['href']}")

else:
    print(f"Failed to retrieve the page. Status Code: {response.status_code}")
