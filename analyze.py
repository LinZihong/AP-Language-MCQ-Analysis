from distill import *
from word_forms.word_forms import get_word_forms
from functools import reduce

def get_flattened_word_forms(word):
    wfs = get_word_forms(word)
    merged = list()
    for k, s in wfs.items():
        merged.extend(s)
    return merged

def load_word_list(filename):
    text = open(filename,'r',errors='ignore').readlines()
    return set([x.strip() for x in text][:5])

def transform_word_list(wlist):
    wf_transformed = list(map(get_flattened_word_forms, wlist))
    merged = list()
    for forms in wf_transformed:
        merged.extend(forms)
    return set(merged)

wlist = load_word_list('Barron_more.txt')
wforms = transform_word_list(wlist)

