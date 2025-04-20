#This function checks if a string is a palindrome
def is_palindrome(cad):
    if(len(cad) == 0):
        return False
    for i in range(len(cad)//2):
        if(cad[i] != cad[-i-1]):
            return False
    return True

character:str = input("Enter a character string: ")

print(f"Is it palindrome?: {is_palindrome(character)}")