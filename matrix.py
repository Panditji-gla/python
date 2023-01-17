row = int(input("Please enter the number of rows\n"))
column = int(input("please enter the number of column\n"))
mat = []
for i in range (row):
    sbls = []
    for j in range (column):
        sbls.append(int(input("Please enter a number\n")))
    mat.append(sbls)

# mat2 = []
# for i in range (row):
#     sbls = []
#     for j in range (column):
#         sbls.append(int(input("Please enter a number\n")))
#     mat2.append(sbls)


for i in range (row):
    for j in range (column):
        print(mat[i][j],end="    ")
    print()

print("\n\n\n")

# dgsum = 0
# if row != column :
#     print("invalid data input")
# else:
#     for i in range (row):
#         dgsum += mat[i][i]
#     print("digonal sum is %d"%dgsum)

# print("\n\n\n")

# adgsum = 0
# if row != column :
#     print("invalid data input")
# else:
#     for i in range (row):
#         for j in range (column):
#             if (j+i) == (row-1):
#                 adgsum += mat[i][j]
#     print("anti digonal sum is %d"%adgsum)

# print("\n\n\n")

# if row != column :
#     print("invalid data input")
# else:
#     for i in range (row):
#         for j in range (column):
#             if j >= i:
#                 print(mat[i][j],end="    ")
#             else:
#                 print("     " ,end="")
#         print()

# print("\n\n\n")

# if row != column :
#     print("invalid data input")
# else:
#     for i in range (row):
#         for j in range (column):
#             if j <= i:
#                 print(mat[i][j],end="    ")
#             else:
#                 print("     " ,end="")
#         print()

# print("\n\n\n")


# for i in range (row):
#     for j in range (column):
#         print(mat2[i][j],end="    ")
#     print()

# print("\n\n\n")

# sum = []

# for i in range (0,row):
#     sbls = []
#     for j in range (0,column):
#         sbls.append(mat[i][j] + mat2[i][j])
#     sum.append(sbls)

# for i in range (row):
#     for j in range (column):
#         print(sum[i][j],end="    ")
#     print()

# print("\n\n\n")

transpose = []
for i in range (row-1,-1,-1):
    sls = []
    for j in range (column-1,-1,-1):
        sls.append(mat[i][j])
    transpose.append(sls)

for i in range (row):
    for j in range (column):
        print(transpose[i][j],end="    ")
    print()

print("\n\n\n")