a = [[1,2,3],[7,3,6],[8,11,13]]
b = [[12,13,17],[6,8,7],[3,4,5]]
for i in range (0,len(a),1):
    for j in range(0,len(a),1):
        print(a[i][j]+b[i][j],end="  ")
    print()
    