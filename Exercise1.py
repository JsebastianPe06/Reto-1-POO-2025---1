#Esta función opera dos números según una opción elegida
def calculadora(a, b, op):
    if(op==1):
        return a+b
    elif(op==2):
        return a-b
    elif(op==3):
        return a*b
    return a/b if(b!=0) else("Error. No se puede dividir entre cero")

#Opciones de menú
op_1:str = "1.suma"
op_2:str = "2.resta"
op_3:str = "3.multiplicación"
op_4:str = "4.división"

#Esta función valida que la opción elegida esté dentro del rango
def validacion_opciones():
    print(f"{op_1}\n{op_2}\n{op_3}\n{op_4}")
    op:int = int(input("Ingrese su opción: "))
    while(op<1 or op>4):
        print(f"{op_1}\n{op_2}\n{op_3}\n{op_4}")
        op:int = int(input("Error. Opción fuera de rango. Ingrese su opción: "))
    return op

opcion:int = validacion_opciones()
num1:int = int(input("Ingrese un número: "))
num2:int = int(input("Ingrese otro número: "))

print(calculadora(num1, num2, opcion))
