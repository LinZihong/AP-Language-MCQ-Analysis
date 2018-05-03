import re

def distill():
    regexStr = r"(?s)\(A\).*?(?=[0-9]|Unauthorized|Commercial)"
    regex = re.compile(regexStr)
    text = open('./pdf/AP Lang 2015.txt', 'r', errors='ignore').read()
    escape = ["\"", "\'", ",", ".", "!", "?", "(A)", "(B)", "(C)", "(D)", "(E)"]
    regexFound = regex.findall(text)

    for i in range(len(regexFound)):
        for char in escape:
            regexFound[i] = regexFound[i].replace(char, "")
        regexFound[i]=regexFound[i].strip()

    return regexFound

def split(arrayFound):
    return [x.split() for x in arrayFound]

# print(distill()[:20])
