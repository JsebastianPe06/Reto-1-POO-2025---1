#Esta función verifica si una cadena es palíndromo
def es_palindromo(cad):
    if(len(cad) == 0):
        return False
    for i in range(len(cad)//2):
        if(cad[i] != cad[-i-1]):
            return False
    return True

cadena:str = input("Ingrese su cadena de caracteres: ")

print(f"Es palíndromo?: {es_palindromo(cadena)}")
