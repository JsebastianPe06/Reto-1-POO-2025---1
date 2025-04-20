# Reto-1-POO-2025---1
Aquí se encuentran los 5 ejercicios descritos en el reto #1 del curso de POO
2025 - 1

## Ejercicios
- [Ejercicio_1:Calculadora]
- [Ejercicio_2:Palíndromo]
- [Ejercicio_3:Números_primos]
- [Ejercicio_4:Mayor_suma]
- [Ejercicio_5:Mismos_caracteres]

## Ejercicio_1:Calculadora
Para este ejercicio simplemente se creo una función que reciba dos números y
según una opción elegida por el usuario realiza una operación, como esta opción
se elige a modo de número se usa una función que se asegura que es número esté
dentro de la opciones y se observa si existe un caso que dé un error para
establecer que la función calculadora envíe el mensaje, en este caso cuando se
divide entre cero.

## Ejercicio_2:Palíndromo
Dado que un palíndromo se lle igual al derecho y al revés, esto implica que si
se lee el primer caracter y el último estos deben ser iguales y así
sucesivamente hasta llegar a la mitad de la palabra, por lo que solo se se crea
una función que haga esto y si encuentra una desigualdad retorna falsos.

## Ejercicio_3:Números_primos
Primero se debe crear un identificador de números primos, como estos solo son
divisibles entre 1 y él mismo, se crea una función que pruebe esta afirmación
sea verdadera usando módulos en números desde hasta la parte entera de la raíz
cuadrada de dicho número (matematicamente se puede probar que si no hay
divisores en ese rango el números es primo), luego, solo se hace otra función
que aplique el identificador en toda la lista del número.

## Ejercicio_4:Mayor_suma
Para obtener la mayor suma de dos número consecutivos en una lista solo hay que
comparar cada suma y guardar la mayor, para hacer este proceso más óptimo se
pensó en una variable que guarde esta suma y que recorra las sumas a modo de
lista ordenada, si se encuentra una suma mayor a la que está guardado la
variable guarda ese valor hasta recorrer todas las sumas y devolver la que
quedó guardada. Se inicializa con la primera suma y continua en la siguente,
esto para que la función no devuelva valores incorrectos.

## Ejercicio_5:Mismos_caracteres
Se sigue una lógica similar de los números primos, crendo un verificador que
compruebe que dos palabras poseen exactamente los mismos caracteres, para esto,
primero se comprueba que las palabras tengan el mismo tamaño, si lo tienen, se
crean copias a modo de listas que permiten manipularlas de mejor manera, el
modo de verificación consiste en que si en amabas palabras hay un caracter
similar, esta caracter se elimina de una de las listas y se compara otro
caracter, se este proceso se termina entonces devuelve verdadero. Luego, se
crea una función que devuelve una lista de listas agrupando las palabras que
cumplen con la condición anterior entre si, por último, con otra función se
eliminan los grupos de una sola palabra.