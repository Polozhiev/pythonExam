import string
from collections import defaultdict

def open_file(filename="pythonExam/input.txt"):
    with open(filename, "r") as file:
        data=file.read()
    return data

def prepare_data(data):
    tab=str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    words = data.translate(tab).split()
    return words

def count(words):
    d = defaultdict(int)
    for word in words:
        d[len(word)] += 1
    return d

def sort_dict(word_dict):
    sorted_tuples = sorted(word_dict.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict

def main():    
    data=open_file()
    words=prepare_data(data)
    word_dict=count(words)
    sorted_dict=sort_dict(word_dict)
    print(sorted_dict)
    #print(list(sorted_dict.values()))

if __name__=="__main__":
    main()