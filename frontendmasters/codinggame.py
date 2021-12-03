import sys
import math
from typing import Collection

# s = input().lower().replace(" ", "")
# d = {}
# for c in s:
#     if c in d:
#         d[c] += 1
#     else:
#         d[c] = 1
# print(" ".join([f"{c}:{d[c]}" for c in d]))

#*#######################################################

# lm,ls = map(int,input().split(":"))
# l=lm*60+ls
# pm,ps = map(int,input().split(":"))
# p=pm*60+ps
# t=int(p/l*15)

#*#######################################################

# print("*****************")
# print(f'*{"-"*t:<15}*')
# print("*****************")

#*#######################################################

# p=input
# print(int(p())+int(p())*(int(p())-1))
# #or
# print(int(input())+int(input())*(int(input())-1))

#*#######################################################

#largest prime number 
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input())
# p = -1
# for i in range(n):
#     m = int(input())

#     if m > p:
#         if is_prime(m):
#             p = m
# print(p)

#*#######################################################

# # 0 - 99 remote up and down button
# n = int(input())
# for i in range(n):
#     a, b = [int(j) for j in input().split()]
#     print(min(abs(a-b), abs(100+a-b), abs(100+b-a)))


#*#######################################################

# n = int(input())
# d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'q':16, 'r':17, 's':18, 'u':19, 'v':20, 'w':21, 'x':22, 'y':23, 'z':24}
# c = ""
# for i in range(n):
#     l = input()
#     if l.isalpha():
#         if l.isupper():
#             l = l.lower()
#         c += str(d.get(l)) + "\n"
# print(c)

# # ? code after optimisation
# for i in [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'q':16, 'r':17, 's':18, 'u':19, 'v':20, 'w':21, 'x':22, 'y':23, 'z':24}.get(input().lower()) for i in range(int(input()))]:
#     if i:
#         print(i)

#*#######################################################

# e_prices = input()
# i_prices = input()
# ep = e_prices.split(' ')
# ip = i_prices.split(' ')
# esum = isum = 0
# for i in range(0, len(ep)):
#     esum += int(ep[i])
# for i in range(0, len(ip)):
#     isum += int(ip[i])
# x = str(int(esum / isum * 100)) + "%"
# print(x)

#*#######################################################

# #?mycode
# t=input()
# s=input()
# a=input()
# x=r=0
# tt=t.split(' ')
# if len(tt)>1:
#     for tx in tt:
#         if len(tx)>=2:
#             r+=1
#     if r==len(tt):
#         x+=1
# ss=s.split(' ')
# if len(ss)>9 and ss[0].isupper():x+=1
# if a.find("BOT") == -1:x+=1
# #add upvote condition #!
# print(x)

# #?Maexel's code
# t,s,a=open(0)
# c=0
# if len(t.split())>1 and all(len(p)>2for p in t.split()):c+=1
# if len(s.split())>9 and s[0].isupper():c+=1
# if not 'BOT'in a:c+=1
# if 'upvote'in''.join((t,s,a)).lower():c=-1
# print(c)

#*#######################################################

# s = input().split(' ')[::-1]
# res = ""
# for word in s:
#     res += word + " "
# print(res)

#? shortest code
# print (" ".join(input().split()[::-1])) 

#*#######################################################

# def is_palindrome(i):
#     x = int(bin(i).replace("0b", ""))
#     tmp = x
#     rev = 0
#     while x > 0:
#         rev = rev * 10 + (x % 10)
#         x = x // 10
#     if tmp == rev:
#         return 1

# n = int(input())
# sum = cpt = 0
# for i in range(1, n):
#     if is_palindrome(i) == 1:
#         sum += i
#         cpt += 1
# print(int(sum/cpt), " is a palindrome in binary") if is_palindrome(int(sum/cpt)) == 1 else print(int(sum/cpt), " is not a palindrome in binary")

#*#######################################################

# a, b, c = [int(i) for i in input().split()]
# if a*a+b*b==c*c:
#     x = math.gcd(a, b, c)
#     print(a//x, b//x, c//x)
# else:
#     print("NOT A TRIPLE")

#*#######################################################

# print(sum(range(int(input()))))

#*#######################################################

# l, w, h = open(0) #!!!!! ctrl + D
# l=int(input())
# w=int(input())
# h=int(input())
# print(2*(h*w)+2*(h*l)+2*(w*l))

#*#######################################################

# a=input
# print(int(a())^int(a())^int(a()))

#*#######################################################

# n = int(input())
# for i in range(n):
#     a, b, c = [int(j) for j in input().split()]
#     if a <= b <= c or c <= b <= a:
#         print(b)
#     elif b <= a <= c or c <= a <= b:
#         print(a)
#     elif a <= c <= b or b <= c <= a:
#         print(c)

# #? omar's solution 
# n = int(input())
# for i in range(n):
#     print(sorted([int(j) for j in input().split()])[1])

#*#######################################################

# a = input()
# n = int(input())
# if a.lower() == "upper" and 0 < n < 27:
#     print(' '.join([chr(x+65)for x in range(n)]))
# elif a.lower() == "lower" and 0 < n < 27:
#     print(' '.join([chr(x+97)for x in range(n)]))
# else:
#     print("ERROR")

# #? 
# case_or_trick = input().lower()
# n = int(input())
# s=""
# if n > 26:
#     s = "ERROR "
# elif case_or_trick=="upper":
#     for i in range(65, 65+n):
#         s+=chr(i)+" "
# elif case_or_trick=="lower":
#     for i in range(97, 97+n):
#         s+=chr(i)+" "
# print(s[:-1])

#*#######################################################

# text = input()
# for c in text:
#     if c.isupper():
#         print(c.lower(), end="")

#*#######################################################

#? 01 Test 1
#20
#18 21
#? 02 Test 2
#100
#97 119
#? Test 3
#1000
#871 179

def collatz_conjecture():
    limit = int(input())
    res = (0, 0)
    for i in range(2, limit+1):
        j = i
        s = 1
        while 1<j:
            j = j/2 if not j%2 else j*3+1
            s+=1
        if res[1] < s:
            res = (i, s)
    print(*res)

collatz_conjecture()