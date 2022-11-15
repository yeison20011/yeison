#YEISON LOPEZ

def llenar_lista(lista,limite):
    
    for i in range (0, limite):
        x = str(input("Dame una palabra para ingresar a la lista: "))
        lista.append(x)
    return (lista)    
        
def buscar_string (lista, palabra):
    contador = 0
    for j in range (len(lista)):
        if (lista[j] == palabra):
            contador += 1        
    return (contador)

def replace (lista):
    x = len(lista)-1
    z = lista [x]
    y = lista[0]
    lista[0] = z
    lista[x] = y
    return (lista) 
     
     
if __name__ == "__main__":
    
    lista_string = []
    
    x = llenar_lista(lista_string,5)
    print (lista_string)
  
    nombre = "messi"
    y = buscar_string (lista_string, nombre)
    print ("La palabra "+ nombre +" se encuentra "+ str(y) + " veces dentro de la lista")
    
    z = replace (lista_string)
    print (z)
    
    
    