import csv

def creacion_matrix (array):
    matrix = []
    lengh = int(input("Dime cuantos usuarios desea registrar: "))
            
    for i in range (lengh):
        array.append ([])
        for j in range (3):
            date = str(input("Digite el "+array[i][j]+" de la persona: "))
            array[i+1].append (date)
        matrix.append (array)
    return (matrix)            

def creando(array, rout):
    
    with open(rout,'w',newline='')as csvfile:
        matrix = creacion_matrix (array)
        writer=csv.writer(csvfile, delimiter=';')
        writer.writerows(matrix)
def leyendo(dire):
    with open(dire,'r',newline='')as csvfile:
        reader=csv.reader(csvfile,delimiter=';')
        for row in reader:
            print(row) 
            
def agregando(dire, creacion):
    with open(dire,'r',newline='')as csvfile:
        reader=csv.reader(csvfile,delimiter=';')
        data=[line for line in reader]
    with open(dire,'w',newline='')as csvfile:
        creation = creacion
        writer=csv.writer(csvfile,delimiter=';')
        writer.writerows(data)
        writer.writerows(creation)            

def eliminando(search, dire):
    with open(dire,'r',newline='')as csvfile:
        reader=csv.reader(csvfile,delimiter=';')
        data=[line for line in reader]
    with open(dire,'w',newline='')as csvfile:
        writer=csv.writer(csvfile,delimiter=';')
        data.pop(search)
        writer.writerows(data)
            

if __name__=="__main__":
    
    array = [['CODIGO', 'NOMBRE', 'APELLIDO']]        
    creation = 0
    rout = str ("Dame la ruta exacta: ")    
    
    print("\n")
    print("""
          1) CREAR ARCHIVO CSV.
          2) LECTURA DE CSV CREADO ANTERIORMENTE.
          3) ACTUALIZAR CSV CREADO ANTERIORMENTE.
          4) ELIMINAR UN DATO DEL CSV.
          5) SALIR
          """)
    option = int(input("OPCION ELEGIDA: "))
    if (option >= 1 and option <= 5):
        if (option == 1):
            print ("\n")
            rout = str(input("Ingrese la ruta exacta para guardar el archivo: "))
            creation = creando(array, rout)
            print("\n")
        elif (option == 2):
            rout = str(input("Ingrese la ruta exacta donde se guardo el archivo: "))
            reading = leyendo (rout)
            print("\n")
        elif (option == 3):
            print ("""
                   1) AGREGAR
                   2) ELIMINAR
                   """)
            op = int(input("OPCION ELEGIDA: "))
            if (op >= 1 and op <= 2):
                if (op == 1):
                    add = agregando (rout, creation)
                    print ("\n")
                elif (op == 2):
                    element = int(input("Posicion del elemento que desea eliminar [][]: "))
                    pop = eliminando (element, rout)
                    print("\n")
        elif (option == 4):
            element = int(input("Posicion del elemento que desea eliminar [][]: "))                    
            pop = eliminando (element, rout)
            print("\n")
        elif (option == 5):
            print ("\n")
            print ("---HAS SALIDO DEL MENU---")                
                
            
    