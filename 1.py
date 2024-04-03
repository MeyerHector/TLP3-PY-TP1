def weird_algohrithm(n):
    array = [n]
    while n != 1: # Mientras n sea distinto de 1 hacer
        
        if n%2==0: # Si n / 2 (si n es impar)
            n = (n//2) # lo divide por dos y reasigna el valor de n
            array.append(n)
        else: # Si n no es par
            n = (n * 3) + 1 # Reasigna el valor de n multiplicandolo por 3 y sumandole uno para que sea par
            array.append(n)
    return array

print(weird_algohrithm(3))
assert weird_algohrithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], 'error en el caso de prueba'
print('Calculo exitoso')
