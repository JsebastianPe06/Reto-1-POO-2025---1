import random

#Esta función compara la sumas de dos números consecutivos
#Retorna la suma más grande
def mayor_suma_consecutiva(lis):
    if(len(lis)<=1):
        return 0
    s = lis[0]+lis[1]
    for i in range(1,len(lis)-1):
        if(s<lis[i]+lis[i+1]):
            s = lis[i]+lis[i+1]
    return s

#Esta función genera una lista de números aleatorios
def generador_lista_numeros(n):
  m = []
  for i in range(n):
    m.append(random.randint(-1000,1000))
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
print(f"La suma más grande es: {mayor_suma_consecutiva(lista_numeros)}")
