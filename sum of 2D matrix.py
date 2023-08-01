matrix1 = [[1,2,3],
          [4,5,6]]


matrix2 = [[7,8,9],
          [10,11,12]]

matrix3= []
if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]) and len(matrix1[1]) == len(matrix2[1]) :
    for i in range(2) :
        for j in range(3):
            matrix3.append((matrix1[i][j] +matrix2[i][j]))

print(matrix3)
            
    
    

           
                

        

