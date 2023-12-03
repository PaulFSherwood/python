import requests, re
from bs4 import BeautifulSoup

def get_words(url):
    # Extract the Hebrew and English words
    hebrew_words = []
    english_words = []

    for cell in soup.select('td.hebrew2, td.eng'):
        if 'hebrew2' in cell['class']:
            hebrew_word = re.search(r'(?<=\>).+?(?=<)', str(cell)).group().strip()
            hebrew_words.append(hebrew_word)
        elif 'eng' in cell['class']:
            english_words.append(cell.text.strip())

    # Print the Hebrew and English words
    eng = "English"
    heb = "Hebrew"
    print(f"{eng[:20]:<20} | {heb[:20]:<20}")
    print("------------------------------------")
    for english, hebrew in zip(english_words, hebrew_words):
        print(f"{english[:20]:<20} | {hebrew[:20]:<20}")

for i in range(1, 31):
    url = f'https://biblehub.com/text/genesis/1-{i}.htm'
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    get_words(soup)
    print("\n")
    if i == 3:
        break