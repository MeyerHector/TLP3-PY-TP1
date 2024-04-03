def palindrome_reorder(letters):
    if any(letters.isupper() for letter in letters) or 'ñ' in letters or not letters.isalpha():
        return 'NO SOLUTION'
    #Defino las variables en una linea para no utilizar mas espacio
    dictionary = {}; cant_par = 0; cant_impar = 0; palindrome = []
    
    #Recorro cada letra de el conjunto de letras que recibe la funcion y las ingreso al diccionario junto a la cantidad de veces que aparece
    for letter in letters:
        cant_letter = letters.count(letter)
        dictionary.update({f'{letter}':cant_letter})
    #Recorro las letras del diccionario y si la letra se encuentra un numero par de veces las ingreso en un array al principio y al final, sino la ingreso en el medio del array
    for letter in dictionary:
        if dictionary[letter] % 2 == 0:
            for _ in range(dictionary[letter] // 2):
                cant_par += 1
                palindrome.insert(0, letter)
                palindrome.append(letter)
        else:
            cant_impar += 1
            palindrome.insert(len(palindrome)//2, letter)
    #Con el contador del for anterior verifico si hay mas de una letra par, devuelvo la funcion con un NO SOLUTION
    if cant_impar > 1:
        return 'NO SOLUTION'
    else:
    #Sino devuelvo el array uniendolo con un join()
        
        return(''.join(palindrome))
    
assert palindrome_reorder("aabbc") == "bacab", "Error en el caso de prueba"
print('Exito', palindrome_reorder("aabbc"))