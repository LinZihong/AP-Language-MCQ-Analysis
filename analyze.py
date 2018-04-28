from distill import *
# from word_forms.word_forms import get_word_forms

def get_flattened_word_forms(word):
    wfs = get_word_forms(word)
    merged = set()
    for k, s in wfs.items():
        merged = merged.union(s)
    return merged

def load_word_list(filename):
    text = open(filename,'r',errors='ignore').readlines()
    return set([x.strip() for x in text])

print(load_word_list('Barron_simplified.txt'))
