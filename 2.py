
def missing_number(n, l):
   # Creo un conjunto con todos los números del 1 al n
   array = set(range(1, n+1))
   
   # Creo un conjunto con los números dados en la lista l
   given_array = set(l)
   
   # Encuentra los números faltantes en el conjunto array
   missing_number = list(array - given_array)  
   
   # Devuelve el primer número faltante si hay alguno, de lo contrario devuelve None
   return missing_number[0] if missing_number else None

assert missing_number(5, [1, 2, 4, 5]) == 3, 'ERROR'

print('EXITO')