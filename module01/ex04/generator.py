import random
import string

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if not text or type(text)!= str:
        print("invalid text")
        return 
    if not sep or isinstance(sep, type(string.punctuation)):
        if sep not in text:
            print("invalid seperator")
            return
    words = text.split(sep)
    l=[]
    if option == 'shuffle':
        for w in words:
            pass
    elif option == 'ordered':
        pass
    elif option == 'unique':
        pass
    else:
        for w in words:
            l.append(w)
