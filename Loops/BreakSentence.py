def bucar_numero_en_lista(num, lista):
    indice = -1
    # Recorre la lista con la funcion enumerate
    for i, item in enumerate(lista):
        if item == num:
            indice = num
            # Romper el bucle
            break
    return indice

print(bucar_numero_en_lista(1, [2, 3, 4, 1, 0]))
print(bucar_numero_en_lista(1, [2, 8, 4, 6, 5]))