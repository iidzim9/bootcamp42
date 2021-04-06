import string
from sys import argv

morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
        '9':'----.', '0':'-----'}

def translator(text):
    code = ""
    if text == "":
        return()
    words = text.split()
    for w in words:
        w = w.upper()
        if not w.isalnum():
            print("ERROR")
            return
        for c in w:
            if c in morse:
                code += morse[c]
            code += ' '
    return code

text = ""
out = ""
for arg in argv[1:]:
    text += arg + ' '
text = text.split()
for w in text:
    out += translator(w) + '/ '
print(out[:-3])