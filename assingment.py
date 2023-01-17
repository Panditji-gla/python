# R = int(input("Please enter the number of rows"))
# C = int(input("Please enter the number of column"))
# def formSpiralMatrix(arr, mat):
# 	top = 0;
# 	bottom = R - 1;
# 	left = 0;
# 	right = C - 1;

# 	index = 0;

# 	while (True):
		
# 		if(left > right):
# 			break;
# 		for i in range(left, right + 1):
# 			mat[top][i] = arr[index];
# 			index += 1;
# 		top += 1;

# 		if (top > bottom):
# 			break;
# 		for i in range(top, bottom+1):
# 			mat[i][right] = arr[index];
# 			index += 1;
# 		right -= 1;

# 		if (left > right):
# 			break;
# 		for i in range(right, left-1, -1):
# 			mat[bottom][i] = arr[index];
# 			index += 1;
# 		bottom -= 1;

# 		if (top > bottom):
# 			break;
# 		for i in range(bottom, top-1, -1):
# 			mat[i][left] = arr[index];
# 			index += 1;
# 		left += 1;
# def printSpiralMatrix(mat):
# 	for i in range(R):
# 		for j in range(C):
# 			print(mat[i][j],end= " ");
# 		print();
# mat= [[0 for i in range(C)] for j in range(R)];
# arr = []
# for i in range(R*C,0,-1):
# 	arr.append(i)
# formSpiralMatrix(arr, mat);
# printSpiralMatrix(mat);

n = int(input("Please enter a number\n"))
k = (2*n)-1
l = 0
h = k - 1
val = n
mat = [[0 for i in range (k)] for j in range (k)]
for i in range (n):
	for j in range (l, h+1):
		mat[i][j]=val
	for j in range (l+1, h+1):
		mat[j][i]=val
	for j in range (l+1, h+1):
		mat[h][j]=val
	for j in range (l+1, h):
		mat[j][h]=val
	l = l+1
	h = h-1
	val = val-1
for i in range (k):
	for j in range (k):
		print(mat[i][j], end=" ")
	print()