

import csv
import re
import time
import psutil

# Function to replace words in a text file
def replace_words(file_path, dictionary, find_words_list):
    replaced_words = {}
    with open(file_path, 'r') as f:
        text = f.read()
        for word in find_words_list:
            if word in dictionary:
                replace_word = dictionary[word]
                pattern = r'\b{}\b'.format(word)
                replace_pattern = replace_word if word.islower() else replace_word.capitalize()
                text, count = re.subn(pattern, replace_pattern, text)
                if count > 0:
                    replaced_words[word] = [replace_word, count]
    with open(file_path[:-4] + '.translated.txt', 'w') as f:
        f.write(text)
    return replaced_words

# # Read the find words list
find_words_list = []
with open('find_words.txt', 'r') as f:
    for line in f:
        find_words_list.append(line.strip())

# Read the French dictionary
dictionary = {}
with open('french_dictionary.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        dictionary[row[0]] = row[1]

# # Replace words in the input file
start_time = time.time()
replaced_words = replace_words('t8.shakespeare.txt', dictionary, find_words_list)
end_time = time.time()
time_taken = end_time - start_time

# # Write the list of replaced words to a CSV file
with open('frequency.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['English word', 'French word', 'Frequency'])
    for word, values in replaced_words.items():
        writer.writerow([word, values[0], values[1]])

# # Write the performance metrics to a text file
process = psutil.Process()
memory_used = process.memory_info().rss / (1024 * 1024)
with open('performance.txt', 'w') as f:
    f.write('Time to process: {:.0f} minutes {:.0f} seconds\n'.format(time_taken // 60, time_taken % 60))
    f.write('Memory used: {:.2f} MB\n'.format(memory_used))
    
# # Write the link to the GitHub repository to a text file
with open('githublink.txt', 'w') as f:
    f.write('https://github.com/KishoreVijayakumar0/Translate-Words-Challenge')
