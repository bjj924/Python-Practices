def a_fuction(a_number):
    # Importo el paquete pdb para debuggear y seteo el breakpoint
    # En consola con la letra l voy a poder ver todo lo que esta antes y despues
    # del breakpoint que estableci
    # Si pongo una variable me devuelve el resultado actual
    # Con la letra n pasa a la siguiente linea (F10 en VS)
    # Con la letra s me meto adentro de la llamada a una funcion (F10 en VS)
    # Con la letra c es el equivalente a poner F5
    import pdb
    pdb.set_trace()
    result = None
    # Si el numero es par
    if a_number % 2 == 0:
        # Si es multiplo de 10
        if a_number % 10 == 0:
            # Devuelve el resultado de dividir el numero por 2
            result = a_number / 2
        # Si es multiplo de 8    
        elif a_number % 8 == 0:
            # Devuelve el resultado de dividir el numero por 4
            result = a_number / 4
        else:
            # Sino le resta 1
            result = a_number - 1
    else:
        # Si es impar y multiplo de 3
        if a_number % 3 == 0:
            # Devuelve el resultado de multiplicar el numero por 11
            result = a_number * 11
        # Si es multiplo de 7
        elif a_number % 7 == 0:
            # Devuelve el resultado de multiplicar el numero por 23
            result = a_number * 23
        else:
            # Sino le suma 1
            result = a_number + 1
    return result

result_1 = a_fuction(20)
print(result_1)
        
