# file = open("copy.txt", "w")
# mai = open("shiva.txt", "r")
# str = mai.read()
# file.write(str)
# mai.close()
# file.close()
file = open("shiva.txt","r+")
str = input()
d = file.read()
dat = d[:11] + str + d[11:]
file.write(dat)
file.close()