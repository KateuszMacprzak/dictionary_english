import json #to open data from json file first we have to import json
from difflib import get_close_matches #to jest stała biblioteka programu, dzięki której możemy wykorzystać funkcję słów bliskoznacznych

data = json. load(open("data.json")) #in data we load the json files 1.plik typu json 2.załadowanie go 3.otwarcie go 4.nazwa pliku

def translate(word): #tworzenie funkcji translate
    word=word.lower() #oznaczenie funkcji word.lower, tak aby system widział każdy wyraz z małej litery
    if word in data: #jeśli słowa istnieje w pliku json
        return data[word]  #treść zwrotna dla warunku-zwrócenie samej "wartości", czyli znaczenia słowa
    elif word.title() in data: #jeśli słowa zaczyna się z dużej litery, np Usa
        return data[word.title()] #treść zwrotna dla warunku
    elif word.upper() in data: #jeśli słowa jest z dużych liter, np USA
        return data[word.upper()] #treść zwrotna dla warunku
    elif word.lower() in data: #to jest to samo co word=word.lower() wyżej
        return data[word.lower()] #treść zwrotna dla warunku
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide=input('press y for yes or n for no: ')
        if decide=='y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide=='n':
            return("So you click the wrong keys or this word doesn't exist")
        else:
            return("You have entered wrong input, please enter just y or n: ")
    else:
        print ("You have entered wrong word, please check it again") #gdy słowo nie istnieje



word =input("Enter the word you want to search: ") #treść menu-użytkownik wprowadza słowo
#print(data["zero"]) #here we check does the data work good or not, we can load all the file or just one part of this, for example word zero
output=translate(word) #treść menu
if type(output)==list: #wprowadzanie nowego warunku, dzięki niemu jeżeli słowo będzie miało, więcej niż jedno znaczenie, będzie wyświetlanie jedno pod drugim, a nie zaraz po
    for item in output: #jest to instrukcja, która jest wykonywana dla każdego ze znaczeń tych słów, dzięki temu jedno po drugim zostaje wykonywane
        print(item)
else:
    print (output) #jeśli jest to tylko jedno znaczenie to program drukuje jego jedno znaczenie

