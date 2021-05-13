#wszystkie słowa mamy w pliku data.json
import json #ponieważ słowa mamy w pliku json musimy zaimportować json 
from difflib import get_close_matches
data=json.load(open("data.json")) #import danych do programu
def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead ?"%get_close_matches(word,data.keys())[0]) #'%s' pozwala nam dodać string w innym stringu
        decide=input("press y for or n for no: ")
        if decide=='y':
            return data(get_close_matches(word,data.keys()[0]))
        elif decide=="n" :
            return("This word does not exist in dicionary")
        else:
            print("You have entered the wrong input please enter just y or n ")
    else:
        print ("This word doesn't exist")

print ("Welcome in dictionary")
word=input("Enter the word you want to search: ") #to jest input, w którym to użytkownik wprowadza do programu słowo
output=translate(word)
if type(output)==list:
    for i in output:
        print (i)
else:
    print(output)
