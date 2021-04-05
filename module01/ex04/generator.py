from random import randint
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
    yields=[]
    if option == 'shuffle':
        l = len(words)
        yields = [None] * l
        nbr=[]
        for w in words:
            r = randint(0, l - 1)
            while r in nbr:
                r = randint(0, l - 1)
            nbr.append(r)
            yields[r] = w
    elif option == 'ordered':
        for w in words:
            yields.append(w)
        yields.sort()
    elif option == 'unique':
        yields = set(words)
    else:
        yields = words
    return yields

# text = "Le Lorem Ipsum est simplement du faux texte."
text = "Lorem Ipsum Lorem Ipsum"
# for word in generator(text, sep=" "):
# for word in generator(text, sep=" ", option="shuffle"):
# for word in generator(text, sep=" ", option="ordered"):
for word in generator(text, sep=" ", option="unique"):
    print(word)

# while len(words):
# 	i = random.randint(0, len(words) - 1)
# 	yields.append(words[i])
# 	words[i] = words[-1]
# 	words.pop()