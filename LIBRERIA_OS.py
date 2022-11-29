import os
#YEISON LOPEZ

def create_array (array):
    for i in range (3):
        user = str(input(f"Dame el usuario numero {i+1}: "))
        array.append (user)
    return (array)

def create_user (array):
    for i in range (len(array)):
        name = str (array[i])
        command_line = str ("adduser " + name)
        os.system (command_line)
        print (f"se ha creado exitosamente el usuario {array[i]}")
        

if __name__=="__main__":
    array = []
    create = create_array (array)
    print (create)
    print ("\n")
    create_user (create)

    
    