# import random, math
# print(random.randrange(100, 999,5))
# print(random.randrange(100000,999999))
# char = ["A","B", "C", "D", "E", "F","G", "H", "K","J", "P"]
# spe = ["@", "^", "*", "(", "&", "$"]
# def passs ():
#     pa = ""
#     pa += random.choice(spe)
#     for i in range(2):
#         pa += random.choice(char)
#     pa += str(random.randrange(1000000,9999999))
#     return pa
# paa = passs()
# print(paa)

# def shiva ():
#     x = random.randrange(1,6)
#     count = 0
#     print(x)
#     while True:
#         s = random.randrange(1,6)
#         if s == x:
#             print(s)
#             count += 1
#             if count == 5:
#                 break
# shiva()
from numpy import *
a = array([[1,2,3,4,9,8,8,9], [5,6,7,8,9,9,9,5]])
print(a)
print(a.ndim)
print(a.shape)
# a = a.flatten()
a= a.reshape(4,4)
# print(a.diagonal)
# print(a.sum())
print(a)
print(a.transpose())
print()