import json
from difflib import get_close_matches

data = json.load(open('data.json'))


# lookup user input in dictionary data set (data.json)
def translate(word):

    if word in data:
        return data[word]
    elif word.title() in data:  # check for word in dictionary with first letter upper case
        return data[word.title()]
    elif word.upper() in data:  # check for word in dictionary with all caps
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yesno = input("'%s' not in dictionary.\nDid you mean '%s' instead? (Y)es (N)o: " % (word, get_close_matches(word, data.keys(), cutoff=0.8)[0]))
        if yesno.lower() == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yesno.lower() == 'n':
            return "The word, %s, doesn't exist in the dictionary. Please double check your input" % word
        else:
            return "We didn't understand your entry"
    else:
        return "The word, %s, doesn't exist in the dictionary. Please double check your input" % word


word = input('Enter word: ')
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

