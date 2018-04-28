import re

regexStr = r"(?s)\(A\).*?(?=[0-9]|Unauthorized|Commercial)"

regex = re.compile(regexStr)

text = open('./pdf/AP Lang 2015.txt', 'r', errors='ignore').read()

escape = ["\"", "\'", ",", ".", "!", "?", "(A)", "(B)", "(C)", "(D)", "(E)"]

for result in regex.findall(text):
    for char in escape:
        result = result.replace(char, "")
    print(result)
