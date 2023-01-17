# num = int(input("Please enter a number\n"))
# if num % 2 != 0:
#     print("Weird")
# else:
#     if num >= 2 and num <= 5:
#         print("Not Weird")
#     elif num >= 6 and num <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")

n = int(input("please enter the number of participant\n"))
score = []
for i in range(n):
    score.append(int(input("Please enter the score\n")))
score.sort()
gt = score[-1]
for i in range(1,n+1):
    if score[-i] != gt:
        print(score[-i])
        break
