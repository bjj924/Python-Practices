# Imprime todos los numeros de las pocisiones 0 a 9
for i in range(10):
    print(i)

# Imprime letra por letra en la cadena de caracteres
for i in 'Hola Mundo!':
    print (i)

# Definision de contador con ciclo for que va sumando 1 cada vez que entra en el bucle
def contador(n):
    c = 0
    for n in range(n):
        c += 1
    return c

print(contador(10))

# Sumatoria de una lista de numeros
def sumatoria(numeros):
    acomulador = 0
    for n in numeros:
        acomulador += n
    return acomulador

print(sumatoria([1,2,3,4,5,6,7,8,9]))