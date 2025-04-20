#This function operate two numbers according to a chosen option
def calculator(a, b, op):
    if(op==1):
        return a+b
    elif(op==2):
        return a-b
    elif(op==3):
        return a*b
    return a/b if(b!=0) else("Error. cannot be divided by zero")

#Options of menu
op_1:str = "1.addition"
op_2:str = "2.subtraction"
op_3:str = "3.multiplication"
op_4:str = "4.division"

#This function validates that the chosen option is within the range 
def validation_options():
    print(f"{op_1}\n{op_2}\n{op_3}\n{op_4}")
    op:int = int(input("Enter your option: "))
    while(op<1 or op>4):
        print(f"{op_1}\n{op_2}\n{op_3}\n{op_4}")
        op:int = int(input("Error. Option out of range. Enter ypur option: "))
    return op

option:int = validation_options()
num1:int = int(input("Enter a number: "))
num2:int = int(input("Enter another number: "))

print(calculator(num1, num2, option))