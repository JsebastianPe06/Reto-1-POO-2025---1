import random

#Esta función comprueba si un número es primo
def es_primo(n):
    if(n <= 1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    return True

#Esta función retorna una lista de números primos según una lista previa
def retorna_primos(lis):
    s = []
    for i in range(len(lis)):
        if(es_primo(lis[i])):
            s.append(lis[i])
    return s

#Esta función genera una lista de números aleatorios
def generador_lista_numeros(n):
  m = []
  for i in range(n):
    m.append(random.randint(0,1000))
  return m

#Esta función se asegura de que un número sea mayor a otro
def es_mayor(n,m,tex):
  while(n<=m):
    n = int(input(tex))
  return n

tamano:int = int(input("Ingrese el número de elementos de la lista: "))
tamano:int = es_mayor(tamano,1,"Error. Ingrese un número mayor a 1: ")

lista_numeros = generador_lista_numeros(tamano)

print(f"lista: {lista_numeros}")
print(f"lista de números primos: {retorna_primos(lista_numeros)}")
