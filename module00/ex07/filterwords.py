import sys

if len(sys.argv) == 3:
    s = sys.argv[1]
    n = sys.argv[2]
    if s.isdigit():
        print("ERROR")
        exit()
    elif n.isdecimal():
        n = int(n)
        s = s.replace(',', ' ')
        words = s.split()
        out = []
        for w in words:
            if len(w) > n:
                out.append(w)
        print(out)
        exit()
print("ERROR")
exit()