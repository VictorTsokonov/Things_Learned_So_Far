import json
from difflib import get_close_matches

filedir = "D:\\CVprojects\\downloaded\\Interactive_Dictionary\\data.json"
data=json.load(open(filedir))

def translate(word):
    word=word.lower();
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes, or N if no : " % get_close_matches(word,data.keys())[0]).upper()
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
            
    else:
        return "The word doesn't exist. Please double check it."

w=input("Enter word to be searched : ")

output=translate(w)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)