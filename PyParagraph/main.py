#Import the necessary files
import re
import os

#Initialize Variables
wordCount = 0
wordCountPattern = '[a-z]+' #pattern for countning words - utilize
sentenceCount = 0
sentenceCountPattern = '[^?!.][?!.]' #pattern for counting sentences - utlize punctiation marks to break
numSentences = 0
averageSentenceLength = 0
totalCharacters = 0
path_to_file = os.path.join('raw_data', 'paragraph_3.txt') #file

#read all of the contents of the file in a variable to be processed
with open(path_to_file) as f:
    contents = f.readlines()

#calculate word count with its pattern
wordCount = len(re.findall(wordCountPattern, str(contents)))
#celculate sentence count with its pattern
sentenceCount = len(re.findall(sentenceCountPattern, str(contents)))

#split the contents into a list of sentences to calculate average
paragraphSplit = re.split("(?<=[.!?]) +", str(contents))
for sentence in paragraphSplit:
    numSentences += 1
    averageSentenceLength += len(re.findall(wordCountPattern, str(sentence)))
    totalCharacters += len(sentence)

#print analysis
print("Total Characters: " + str(totalCharacters))
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count: " + str(totalCharacters/wordCount))
print("Average Sentence Length: " + str(averageSentenceLength/numSentences))

