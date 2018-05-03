import re

def distill(txt_file):
    regexStr = r"(?s)\(A\).*?(?=[0-9]|Unauthorized|Commercial)"
    regex = re.compile(regexStr)
    text = open(txt_file, 'r', errors='ignore').read()
    escape = ["\"", "\'", ",", ".", "!", "?", "(A)", "(B)", "(C)", "(D)", "(E)"]
    regexFound = regex.findall(text)

    for i in range(len(regexFound)):
        for char in escape:
            regexFound[i] = regexFound[i].replace(char, "")
        regexFound[i]=regexFound[i].strip()

    return regexFound

def split(arrayFound):
    return [x.split() for x in arrayFound]

def get_answer_words(txt_file):
    return split(distill(txt_file))
