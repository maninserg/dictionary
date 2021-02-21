import json
from difflib import get_close_matches
from phonemizer import phonemize
import shutil



def get_phonetic(w):
        return phonemize(w,backend="espeak")


def get_description(w):
    data = json.load(open("dictionary.json"))
    w = w.lower()
    if w in data:
        return (w, get_phonetic(w), data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return (get_close_matches(w, data.keys())[0],
                    get_phonetic(get_close_matches(w, data.keys())[0]),
                    data[get_close_matches(w, data.keys())[0]])
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist. Please double check it"

def pretty_print_description(w, ph, descrip):
    width = shutil.get_terminal_size().columns
    title = "{} - /{}/".format(w, ph)
    border = "=" * len(title)
    print(border.center(width))
    print(title.center(width))
    print(border.center(width))
    print("")
    print(descrip)
    print("")
    print("+" * width)
    print("")


def main():
    word = input("Enter word: ")
    tp = get_description(word)
    if  len(tp) == 3:
        pretty_print_description(tp[0], tp[1], tp[2])
    else:
        print(tp)


if __name__ == "__main__":
    while True:
        main()
