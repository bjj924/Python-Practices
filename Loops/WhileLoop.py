def suma_n(n):
    #Suma numeros de uno a n
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result

print(suma_n(5))

def infinite_loop():
    # Imprime el numero 1 infinitas veces
    i = 1
    while i <= 10:
        print(i, end=' ')

infinite_loop()
