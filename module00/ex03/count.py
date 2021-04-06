import string

def text_analyzer(*arg):
    """
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
    """
    if len(arg) == 0:
        s = input("What is the text to analyse?\n>> ")
    elif len(arg) >= 2:
        print("ERROR")
        return
    else:
        s = arg[0]
        lower = 0
        upper = 0
        space = 0
        punct = 0
        char = 0
        for c in s:
            lower += c.islower()
            upper += c.isupper()
            space += c.isspace()
            punct += 1 if c in string.punctuation else 0
        char = lower + upper + space + punct
        print("the text contains %d characters:" % char)
        print("- %d upper letters" % upper)
        print("- %d lower letters" % lower)
        print("- %d punctuation marks" % punct)
        print("- %d spaces" % space)

# print(text_analyzer.__doc__)