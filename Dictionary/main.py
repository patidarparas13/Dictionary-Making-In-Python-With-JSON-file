import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did You Mean %s instead? Enter Y if yes,Else N for No. :" % (get_close_matches(word,data.keys(),cutoff=0.8))[0])
        if yn == "Y" or "y":
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn == "N" or "n":
            return "The Word Does Not Exist.Please Double Check it."
        else:
            return "We Doen't Understand your Query."
    else:
        return ("There is no word like this.Please Double Check it.")

word = input("Enter The Word :")
output = translate(word)
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)