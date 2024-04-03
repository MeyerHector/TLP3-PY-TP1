def number_spiral(row, col):
    #Si la fila son iguales devuelvo la formula row^2 - row + 1
    if row == col:
        return row**2 - row + 1
   
   #Si la fila es mayor a la columna pregunto si la fila es par (devuelvo fila^2 - col + 1) o sino devuelvo ((fila - 1)^2 + columna)
    if row > col:
        if row % 2 == 0:
            return row**2 - col + 1
        else:
            return (row - 1)**2 + col
    #si no es ninguno de los casos pregunto si la columna es par y si es asi devuelvo ((columna - 1)^2 + fila), o si no es par devuelvo (columna^2 + 1 - fila )
    else: 
        if col % 2 == 0:
            return (col - 1)**2 + row
        else:
            return col**2 + 1 - row

assert number_spiral(1, 5) == 25, "Error en el caso de prueba"

print("EXITO")