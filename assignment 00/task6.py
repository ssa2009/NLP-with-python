#Instructions:Provide a text prompt “Type a regular plural noun and hit Enter: ”. Then print the 2 grammatical singular version of the same noun.
word = input("enter a regular plural noun and click enter: ")
if word.endswith("es"):
    singular = word[:-2]
elif word.endswith("s"):
    singular = word[:-1]
else:
    singular = word
print(singular)