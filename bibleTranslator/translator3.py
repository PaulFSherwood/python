import requests, re, json
from bs4 import BeautifulSoup


# genesis/{chapter_number}-{verse_number}.htm
# Genesis chapter:verse counts
genesis_verse_counts = {
    1: 31,
    2: 25,
    3: 24,
    4: 26
}
#     5: 32,
#     6: 22,
#     7: 24,
#     8: 22,
#     9: 29,
#     10: 32,
#     11: 32,
#     12: 20,
#     13: 18,
#     14: 24,
#     15: 21,
#     16: 16,
#     17: 27,
#     18: 33,
#     19: 38,
#     20: 18,
#     21: 34,
#     22: 24,
#     23: 20,
#     24: 67,
#     25: 34,
#     26: 35,
#     27: 46,
#     28: 22,
#     29: 35,
#     30: 43,
#     31: 55,
#     32: 32,
#     33: 20,
#     34: 31,
#     35: 29,
#     36: 43,
#     37: 36,
#     38: 30,
#     39: 23,
#     40: 23,
#     41: 57,
#     42: 38,
#     43: 34,
#     44: 34,
#     45: 28,
#     46: 34,
#     47: 31,
#     48: 22,
#     49: 33,
#     50: 26
# }

# Create an empty dictionary to store the words
word_dict = {}

def get_words(url):
    # Extract the Hebrew and English words
    hebrew_words = []
    english_words = []

    for cell in soup.select('td.hebrew2, td.eng'):
        if 'hebrew2' in cell['class']:
            hebrew_word = re.search(r'(?<=\>).+?(?=<)', str(cell)).group().strip()
            hebrew_words.append(hebrew_word)
        elif 'eng' in cell['class']:
            english_word = cell.text.strip()
            english_words.append(english_word)
            # Add the words to the dictionary
            word_dict[english_word] = hebrew_word

    # Print the Hebrew and English words
    eng = "English"
    heb = "Hebrew"
    print(f"{eng[:20]:<20} | {heb[:20]:<20}")
    print("------------------------------------")
    for english, hebrew in zip(english_words, hebrew_words):
        print(f"{english[:20]:<20} | {hebrew[:20]:<20}")

def print_dictionary(word_dict):
    # Print the first 10 words in the dictionary
    for i, (english_word, hebrew_word) in enumerate(word_dict.items()):
        print(f"{english_word}: {hebrew_word}")
        # if i == 9:
        #     break

# Save a dictionary to a file
def save_dictionary_to_file(word_dict, file_path):
    with open(file_path, 'w') as file:
        json.dump(word_dict, file, indent=4)

# Load a dictionary from a file
def load_dictionary_from_file(file_path):
    with open(file_path, 'r') as file:
        word_dict = json.load(file)
    return word_dict



for chapter_num, num_verses in genesis_verse_counts.items(): #i in range(1, 31):
    for verse_num in range(1, num_verses + 1):
        url = f'https://biblehub.com/text/genesis/{chapter_num}-{num_verses}.htm'

        # Send a GET request to the URL
        response = requests.get(url)

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the text from the verse
        # verse_text = soup.select_one('.text > span').text.strip()

        # Extract the words and store them in the dictionary
        get_words(soup)


save_dictionary_to_file(word_dict, 'word_dict.json')
word_dict2 = load_dictionary_from_file('word_dict.json')

print_dictionary(word_dict2)






# exodus/1-1.htm
# leviticus/1-1.htm
# numbers/1-1.htm
# deuteronomy/1-1.htm
# joshua/1-1.htm
# judges/1-1.htm
# ruth/1-1.htm
# 1_samuel/1-1.htm
# 2_samuel/1-1.htm
# 1_kings/1-1.htm
# 2_kings/1-1.htm
# 1_chronicles/1-1.htm
# 2_chronicles/1-1.htm
# ezra/1-1.htm
# nehemiah/1-1.htm
# esther/1-1.htm
# job/1-1.htm
# psalms/1-1.htm
# proverbs/1-1.htm
# ecclesiastes/1-1.htm
# songs/1-1.htm
# isaiah/1-1.htm
# jeremiah/1-1.htm
# lamentations/1-1.htm
# ezekiel/1-1.htm
# daniel/1-1.htm
# hosea/1-1.htm
# joel/1-1.htm
# amos/1-1.htm
# obadiah/1-1.htm
# jonah/1-1.htm
# micah/1-1.htm
# nahum/1-1.htm
# habakkuk/1-1.htm
# zephaniah/1-1.htm
# haggai/1-1.htm">
# zechariah/1-1.htm
# malachi/1-1.htm