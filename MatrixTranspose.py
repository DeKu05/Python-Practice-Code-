'''Matrix Transpose
	Input:
		1 2 3
		4 5 6
	Output:
		1 4
		2 5
		3 6'''

arr = [[1,2,3],[4,5,6]]

result = []
for i in range(len(arr[0])):      # columns
    row = []
    for j in range(len(arr)):     # rows
        row.append(arr[j][i])
    result.append(row)

print(result)