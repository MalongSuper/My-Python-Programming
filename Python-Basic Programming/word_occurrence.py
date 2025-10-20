import string

text = ("Egypt is a developing country with the second-largest economy in Africa. "
        "It is considered to be a regional power in the Middle East, North Africa and the Muslim world, "
        "and a middle power worldwide. "
        "Islam is the official religion and Arabic is official language.")

text = text.translate(str.maketrans('', '', string.punctuation))

# Write the file
with open("Txt Files/Egypt.txt", "w") as f:
    f.write(text.lower())

text_list = []  # The list to obtain the word from the text
text_dict = {}  # The dictionary
with open("Txt Files/Egypt.txt", "r") as read_file:
    for read in read_file:
        # Iterate through each text in the file
        for text in read.split():
            text_list.append(text)

# Iterate through each word in the list to find its occurrence
for i in text_list:
    # Append to the dictionary
    text_dict[i] = text_list.count(i)

# Show the dictionary
print("All words and their occurrence")
for key, values in text_dict.items():
    print(f"+ Word: {key}, Count: {values}")

# Get max values
max_values = max(text_dict.values())
# Find the word with most count and return it
print("Words with maximum occurrence")
for key, values in text_dict.items():
    if values == max_values:
        print(f"+ Word: {key}, Count: {values}")
