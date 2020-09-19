def es_primo(n):
    resultado = True
    for div in range(2, n):
        if n % div == 0:
            resultado = False
            break
    return resultado

print(es_primo(13))