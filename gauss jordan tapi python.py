import random
from random import randint
def printmat(matrix):
    print("")
    for i in range(a):
        for j in range(a+1):
            if j < a:
                print(matrix[i][j],end=" ")
            else: 
                print(" | ",matrix[i][j],end=" ")
        print("")
def checksolution():
    no_solution = False
    global index_ns
    index_ns = 0
    nullcount = 0
    for i in range(a):
        for j in range(a):
            if augmat[i][j] == 0:
                nullcount +=1
        if nullcount < a:
            nullcount = 0
        else:
            no_solution = True
            index_ns = i 
            break
    return(no_solution)
def inputmatrix():
    for i in range(a):
        for j in range(a):
            augmat[i][j]= float(input(f"masukkan element[{i+1}][{j+1}]: "))
    for i in range(a):
        augmat[i][a]= float(input(f"masukkan augmented element[{i+1}]: "))
def gauss_jordan_solver(augmented_matrix):
    num_equations = len(augmented_matrix)
    num_variables = len(augmented_matrix[0]) - 1
    
    for col in range(num_variables):
        pivot_row = col
        
        # Find a non-zero pivot row
        while pivot_row < num_equations and augmented_matrix[pivot_row][col] == 0:
            pivot_row += 1
            
        if pivot_row == num_equations:
            continue
        
        # Swap rows to bring the pivot row to the top
        augmented_matrix[col], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[col]
        
        # Scale the pivot row to have a leading 1
        pivot_value = augmented_matrix[col][col]
        for j in range(col, num_variables + 1):
            augmented_matrix[col][j] /= pivot_value
        
        # Eliminate other rows
        for row in range(num_equations):
            if row != col:
                factor = augmented_matrix[row][col]
                for j in range(col, num_variables + 1):
                    augmented_matrix[row][j] -= factor * augmented_matrix[col][j]
    global solution
    solution = [row[-1] for row in augmented_matrix]
    return solution
def kentut():
    if (checksolution() == True) and (augmat[index_ns][a]== 0):
        print ("solusi tak hingga")
    elif (checksolution() == True) and (augmat[index_ns][a]!= 0):
        print ("tidak ada solusi")
    else:
        print("")
        print("matrix augmented: ")
        printmat(augmat)
        gauss_jordan_solver(augmat)
        MET()
def MET():
    
    matrix_echelon_tereduksi  = [[0 for i in range(a+1)]for j in range(a)]
    for i in range (a):
        matrix_echelon_tereduksi[i][i] = 1
        matrix_echelon_tereduksi[i][a] = round(solution[i],4)
    print("")
    print("matrix echelon tereduksi: ")
    printmat(matrix_echelon_tereduksi)  
a = int(input("masukkan jumlah variabel: \n"))
augmat = [[random.randint(0,9) for i in range(a+1)]for j in range(a)]
inputmatrix()
kentut()


