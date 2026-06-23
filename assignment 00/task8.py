#Instructions:Prompt the user to type in a complete sentence and hit Enter. Then display the average word length of the sentence as a floating point number. Disregard punctuation
import re
sentence = input("type a complete sentence and click enter: ")
words = re.findall(r"\w+",sentence)
total_length = 0
for word in words:
    total_length += len(word)
average = total_length/len(words)
print(float(average))