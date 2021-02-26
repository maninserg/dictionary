import json
from phonemizer import phonemize
import shutil


def get_available_keys_for_phrasal_verb(v, d):
    list_keys = list(d[v].keys())
    list_keys_key = []
    for key in list_keys:
        list_key = []
        if isinstance(d[v][key], dict):
            list_key = list(d[v][key].keys())
        list_keys_key.append(list_key)
    return list_keys, list_keys_key


def get_article_for_phrasal_verb(v, k, d):
    dict_article = {}
    for i, ki in enumerate(k[0]):
        if len(k[1][i]) == 0 and isinstance(d[v][ki], list):
            dict_article[ki] = d[v][ki]
        elif len(k[1][i]) == 0 and not isinstance(d[v][ki], list):
            dict_article[ki] = d[v][ki]
        elif len(k[1][i]) > 0:
            list_j = []
            for j,kj in enumerate(k[1][i]):
                for w, kw in enumerate(k[1][i][j]):
                    list_w = list(d[v][ki][kj].keys())
                    list_j.append(list_w)
            flat_list = []
            for m in list_j:
                for item in m:
                    flat_list.append(item)
            dict_article[ki] = flat_list
    return dict_article

def get_phonetic(w):
        return phonemize(w,backend="espeak")

def pretty_print_article_phrasal_verb(v, pronon, dict_article):
    width = shutil.get_terminal_size().columns
    title = "{} - /{}/".format(v, pronon)
    border = "=" * len(title)
    print(border.center(width))
    print(title.center(width))
    print(border.center(width))
    print("")
    for key in dict_article:
        if isinstance(dict_article[key], list):
            str_inf = " -*- ".join(dict_article[key])
            print(" {} : {}".format(key.upper(), str_inf))
        else:
            print(" {} : {}".format(key.upper(), dict_article[key]))
    print("")
    print("+" * width)
    print("")


def main():
    verb = "1"
    data = json.load(open("phrasal.verbs.build.json"))
    while verb != "0":
        verb = input("Enter word(or enter '0' and put 'Enter' for EXIT): ")
        if  not verb.isdigit():
            keys = get_available_keys_for_phrasal_verb(verb, data)
            dict_article = get_article_for_phrasal_verb(verb, keys, data)
            pronon = get_phonetic(verb)
            pretty_print_article_phrasal_verb(verb, pronon, dict_article)
        elif verb.isdigit() and verb == "0":
            print("Good luck, my friend")

if __name__ == "__main__":
    main()
