# sumatoria de los primeros n numeros pares
def sumatoria_par(num):
    # acomulador donde se suman todos los resultados
    acomulador = 0
    # Contador incrumental para recorrer hasta que el ciclo llegue al numero
    i = 0
    # variable incremental para determinar los pares de 2 en 2
    curr = 2

    while i <= num:
        # sumatoria
        acomulador += curr
        # pasa al siguiente par
        curr += 2
        # aumenta el contador
        i = i + 1
    return acomulador

print(sumatoria_par(49))
