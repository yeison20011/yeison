# yeison
from copy import copy

def create_matrix ():
    matriz = []
    print ("\n")
    nfilas = 0
    ncolumnas = 1
    
    while (nfilas != ncolumnas):
        nfilas = int(input("Dime el numero de filas que tendra la matriz: "))
        ncolumnas = int(input("Dime el numero de columnas que tendra la matriz: "))
        if (nfilas != ncolumnas):
            print ("\n")
            print ("PARA HALLAR UNA MATRIZ INVERSA DEBES INGRESAR UNA MATRIZ CUADRADA. VUELVE A INGRESAR LAS DIMENSIONES DE LA MATRIZ.")
            print ("\n")
            
    for i in range (nfilas):
        fila = []
        for j in range(ncolumnas):
            elemento = int(input(f"Dame el valor a ingresar en la fila {i+1}, columna {j+1} de la matriz: "))
            fila.append(elemento)
        
        matriz.append(fila)
    
    return (matriz)  

def creacion_matriz ():
    print ("\n")
    nfilas = int(input("Dime el numero de filas que tendra la matriz: "))
    ncolumnas = int(input("Dime el numero de columnas que tendra la matriz: "))
    
    mat = []
    
    for i in range (nfilas):
        fila = []
        for j in range(ncolumnas):
            elemento = int(input(f"Dame el valor a ingresar en la fila {i+1}, columna {j+1} de la matriz: "))
            fila.append(elemento)
        
        mat.append(fila)
            
    return (mat)    

def imprimir_matriz (matriz):
    for fila in matriz:
        for k in range (len(fila)):
            if (k == len(matriz)): print ("   |", end=' ')
            print ("{0:8.2f}".format(fila[k]), end=' ')
        print ()
    print ()        

def inversa (new_matrix, matriz):
    print ("\n")
    print ("---MATRIZ ORIGINAL---")
    print ("\n")
    imprimir_matriz (matriz)
    
    
    for fila in range (len(new_matrix)):
        for columna in range (len(new_matrix)):
            if (fila == columna):
                new_matrix[fila].append (1)
            else:
                new_matrix[fila].append (0)
    
    print ("\n")
    print ("         ---MATRIZ ORIGINAL CON LA IDENTIDAD---")
    print ("\n")
    imprimir_matriz (new_matrix)                
    print ("\n")            
    
    print ("    ----COLOCAR CEROS EN LA PARTE DE ABAJO---")
    for pivote in range (len(new_matrix)-1):
        if (new_matrix[pivote][pivote] == 0):
            print ("Pivote con valor 0:", pivote, " hay que buscar una fila para cambiarla")
            
            for fila in range (pivote + 1, len(new_matrix)):
                if (new_matrix[fila][pivote] != 0):
                    print ("Sumar la fila: pivote: ", pivote, ", fila: ", fila)
                    for columna in range (pivote, len(new_matrix[fila])):
                        new_matrix[pivote][columna] = (new_matrix[pivote][columna]) + (new_matrix[fila][columna])
                    imprimir_matriz (new_matrix)
                    break
                
            if (new_matrix[pivote][pivote] == 0):
                return (print("NO TIENE INVERSA ESTA MATRIZ"))
        for fila in range (pivote + 1, len(new_matrix)):
            factor = (new_matrix[fila][pivote]) / (new_matrix[pivote][pivote])
            print ("Pivote: ", pivote, ", fila: ", fila, ", factor: ", new_matrix[fila][pivote], "/", new_matrix[pivote][pivote], "=", factor)
            
            if (factor != 0):
                for columna in range (pivote, len(new_matrix[fila])):
                    new_matrix[fila][columna] = (new_matrix[fila][columna]) - ((new_matrix[pivote][columna]) * (factor)) 
            
            imprimir_matriz (new_matrix)
    
     
    print ("\n")        
    print ("    ---COLOCAR CEROS EN LA PARTE DE ARRIBA---")
    print ("\n")
    
    for fila in range (len(new_matrix)):
        print ("Mirando fila: ", fila)
        for columna in range (fila + 1, len(new_matrix)):
            print ("Mirando fila:", fila, ", columna: ", columna)
            if (new_matrix[columna][columna] != 0):
                factor  = (new_matrix[fila][columna]) / (new_matrix[columna][columna])
                print ("Factor: ", new_matrix[fila][columna], "/", new_matrix[columna][columna], "=", factor)
                
                for colAux in range (columna, len(new_matrix)*2):
                    new_matrix[fila][colAux] -= new_matrix[columna][colAux] * factor 
                imprimir_matriz (new_matrix)
            else:
                print ("Nada que hacer porque ya es cero")
    imprimir_matriz (new_matrix)
    

    print ("\n")
    print ("    ---PONIENDO UNO EN LA DIAGONAL PRINCIPAL---") 
    print ("\n")
    
    for fila in range (len(new_matrix)):
        factor = new_matrix[fila][fila]
        for columna in range (len(new_matrix[fila])):
            new_matrix[fila][columna] /= factor 
    imprimir_matriz (new_matrix)
    
    
    print ("\n")
    print ("     ---ELIMINANDO LA MATRIZ IDENTIDAD DE LA IZQUIERDA---")
    print ("\n")
    
    for fila in range (len(new_matrix)):
        new_matrix[fila] = new_matrix[fila][len(new_matrix):]
    
    return (new_matrix)     

def comprobacion (matrizA, matrizB):
  
    m = len (matrizA)
    n = len (matrizA[0])
    p = len (matrizB[0])
    
    M = []
    for i in range (m):
        M.append ([0] * p)
        
    for i in range (m):
        for j in range (p):
            M[i][j] = 0 
            for r in range(n):
                 M[i][j] += matrizA[i][r] * matrizB[r][j]
    return (M)

def multiplicacion_matrices (matriz1, matriz2):

    columnas1 = comprobacion_columnas (matriz1)
    
    filas2 = comprobacion_filas (matriz2)
    
    new_matriz = []
    
    if (columnas1 == filas2):
        
        for h in range (len(matriz1)):
            new_matriz.append ([])
            for x in range (len(matriz2[0])):
                new_matriz[h].append (0)
            
        print ("SI SE PUEDE REALIZAR LA MULTIPLICACION ENTRE LAS MATRICES")
        
        for i in range (len(matriz1)):
            for j in range (len(matriz2[0])):
                for k in range (len (matriz1[0])):
                    new_matriz [i] [j] += matriz1 [i][k] * matriz2 [k][j]    
        return (new_matriz)
    print ("NO SE PUEDE REALIZAR LA MULTIPLICACION ENTRE LAS MATRICES DEBIDO A QUE EL NUMERO DE FILAS DE LA PRIMERA NO ES IGUAL AL NUMERO DE COLUMNAS DE LA SEGUNDA")
   
def comprobacion_filas (matriz):
    
    contador = 0
    
    for i in range (len(matriz)):
        contador += 1
    return (contador)    
    
def comprobacion_columnas (matriz):
    
    contador = 0
    
    for i in range (1):
        for j in range (len(matriz[i])):
            contador += 1 
    return (contador)      

def suma_matrices (matriz1, matriz2):
    
    suma_ma = []
    
    for i in range (len(matriz1)):
        fila = []
        for j in range (len(matriz1 [i])):
            fila.append (matriz1 [i] [j] + matriz2 [i] [j])
        
        suma_ma.append (fila)
    
    return (suma_ma)               
            
if __name__=="__main__":
    matriz = []
    new_matrix = copy (matriz)
    menu = False
    
    
    while (menu == False):
        print ("\n")
        print ("------MENÚ DE MATRICES------")
        print ("\n")
        print ("""
                1) CREAR MATRIZ 
                2) HALLAR MATRIZ INVERSA
                3) SALIR DEL MENÚ
                """)
        op = int(input("Dime la opcion que elegiste: "))
        if (op > 0 and op < 4):
            if (op == 1):
                print ("\n")
                print ("HAS ELEGIDO CREAR MATRIZ. AHORA, ¿QUE DESEAS HACER?")
                print ("\n")
                print ("""
                        1) HALLAR MATRIZ INVERSA
                        2) MULTIPLICACION DE MATRICES
                        3) SUMA DE MATRICES                   
                       """)
                op2 = int(input("Dime la opcion que elegiste: "))
                if (op2 > 0 and op2 < 5):
                    if (op2 == 1):  
                        matriz = create_matrix ()
                        new_matrix = copy (matriz) 
                        x = inversa (new_matrix, matriz)  
                        print ("\n")
                        print ("LA INVERSA DE LA MATRIZ INGRESADA POR METODO DE GAUSS JORDAN ES: ")
                        print ("\n")
                        imprimir_matriz (x)
                        print ("\n")
                        print ("""
                                ¿DESEA HACER LA COMPROBACION?
                                1) SI
                                2) NO
                                """)
                        com = int(input("Dime la opcion que elegiste: "))
                        if (com > 0 and com < 3):
                            if (com == 1):
                                print ("\n")
                                print ("COMPROBACION DE MATRIZ INVERSA")
                                print ("\n")  
                                print ("ASEGURESE DE INGRESAR LA MISMA MATRIZ ORIGINAL")
                                matrizA = create_matrix ()
                                x = comprobacion  (matrizA, new_matrix)
                                print ("MATRIZ IDENTIDAD RESULTADO DEL PRODUCTO ENTRE LA MATRIZ INGRESADA Y LA INVERSA DE LA MISMA")
                                print ("\n")
                                imprimir_matriz (x)
                            else:
                                print ("REGRESANDO AL INICIO...")
                    elif (op2 == 2):
                        print ("\n")
                        print ("RECUERDE QUE EL NUMERO DE COLUMNAS DE LA PRIMERA DEBE SER IGUAL AL NUMERO DE FILAS DE LA SEGUNDA")
                        print ("\n")
                        A = creacion_matriz ()
                        B = creacion_matriz ()
                        res = multiplicacion_matrices (A, B)
                        print ("EL PRODUCTO ENTRE LAS DOS MATRICES ES: ")
                        imprimir_matriz (res)    
                    
                    elif (op2 == 3):
                        print ("\n")
                        print ("RECUERDE QUE PARA SUMAR MATRICES, ESTAS DEBEN SER DEL MISMO TAMAÑO")
                        A = creacion_matriz ()
                        B = creacion_matriz ()
                        x = suma_matrices (A, B)
                        print ("\n")
                        print ("LA SUMA ENTRE LAS MATRICES INGRESADAS ES: ")
                        imprimir_matriz (x)
                        
            elif (op == 2):
                matriz = create_matrix ()
                new_matrix = copy (matriz) 
                x = inversa (new_matrix, matriz)    
                print ("\n")
                print ("LA INVERSA DE LA MATRIZ INGRESADA POR METODO DE GAUSS JORDAN ES: ")
                print ("\n")
                imprimir_matriz (x)
                print ("\n")
                print ("""
                       ¿DESEA HACER LA COMPROBACION?
                       1) SI
                       2) NO
                       """)
                com = int(input("Dime la opcion que elegiste: "))
                if (com > 0 and com < 3):
                    if (com == 1):
                        print ("\n")
                        print ("COMPROBACION DE MATRIZ INVERSA")
                        print ("\n")  
                        print ("ASEGURESE DE INGRESAR LA MISMA MATRIZ ORIGINAL")
                        matrizA = create_matrix ()
                        x = comprobacion  (matrizA, new_matrix)
                        print ("MATRIZ IDENTIDAD RESULTADO DEL PRODUCTO ENTRE LA MATRIZ INGRESADA Y LA INVERSA DE LA MISMA")
                        print ("\n")
                        imprimir_matriz (x)
                    else:
                        print ("REGRESANDO AL INICIO...")      
            elif (op == 3):
                menu = True 
                print ("\n")
                print ("HAS SALIDO DEL MENÚ")  
                print ("\n") 
        
        else:
            print ("HAS ELEGIDO UNA OPCION INCORRECTA")    
