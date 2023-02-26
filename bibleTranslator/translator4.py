from pythonbible import bible
import json

# Create an empty dictionary to store the text of the Bible
bible_dict = {}

# Create a Bible object for the Hebrew Bible (Tanakh)
hebrew_bible = bible(version='tanakh')

# Loop over all the books and chapters in the Bible
for book_name in hebrew_bible.books:
    for chapter_num in range(1, hebrew_bible.num_chapters(book_name) + 1):
        # Retrieve the text of the chapter
        chapter_text = hebrew_bible.get(book_name, chapter_num)

        # Add the chapter text to the dictionary
        if book_name not in bible_dict:
            bible_dict[book_name] = {}
        bible_dict[book_name][chapter_num] = chapter_text

# Save the Bible dictionary to a file in JSON format
with open('bible.json', 'w') as file:
    json.dump(bible_dict, file)
