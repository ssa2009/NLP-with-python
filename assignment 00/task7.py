#Instructions:Prompt the user to type in a complete sentence and hit Enter. Then display each word of the sentence on a separate line. Consider punction such as period, comma, exclamation, or question to be stand alone word tokens of their own. For example, “The boy bit the dog, then left.” Would result in: The boy bit the dog , then left .
import re 
sentence = input("type in a complete sentence then click enter:")
tokens = re.findall(r"\w+|[.,!?]",sentence)
for token in tokens:
    print(token)