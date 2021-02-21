import json
from difflib import get_close_matches
from phonemizer import phonemize



def get_phonetic(w):
        return phonemize(w,backend="espeak")


def get_description(w):
    data = json.load(open("dictionary.json"))
    w = w.lower()
    if w in data:
        return (get_phonetic(w), data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return (get_phonetic(get_close_matches(w, data.keys())[0],
                                 data[get_close_matches(w, data.keys())[0]]))
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist. Please double check it"

def main():
    word = input("Enter word: ")
    print(get_description(word)[0])
    print(get_description(word)[1])

if __name__ == "__main__":
    while True:
        main()
