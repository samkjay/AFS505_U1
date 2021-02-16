rows, cols = (30, 80)
arr = [[0 for i in range(cols)] for j in range(rows)]

arr_prnt = [["*" for i in range(cols)] for j in range(rows)]
arr_prnt[0][0] = 1

#a = '*'
#b = '-'

for i in range(cols):
    for j in range(rows):
        if arr[j][i] == 1:
            arr_prnt[j][i] = '*'
        else:
            arr_prnt[j][i] = '-'


for row in arr_prnt:
    print(*row, sep ='')


if sum([1==1,2==1, 2==2]) == 2:
    print("y")
else:
    print("N")
