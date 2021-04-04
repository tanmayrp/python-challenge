import re
import os

wordCount = 0
wordCountPattern = '[a-z]+'
sentenceCount = 0
sentenceCountPatter = '[^?!.][?!.]'
# re.split("(?<=[.!?]) +", paragraph)

path_to_file = os.path.join('raw_data', 'paragraph_1.txt')

with open(path_to_file) as f:
    contents = f.readlines()

wordCount = len(re.findall(wordCountPattern, str(contents)))
sentenceCount = len(re.findall(sentenceCountPatter, str(contents)))

print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count: ")
print("Average Sentence Length: ")

