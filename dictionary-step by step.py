import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead ?"%get_close_matches(word,data.keys())[0])
        decide=input("Print y for yes or n for n: ")
        if decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            print("Oops, so this word does not exist or you click the wrong buttom")
    else:
        print("This word does not exist")
word=input("Enter the word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
