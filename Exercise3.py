import random

#This function checks if a number is prime
def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i == 0):
            return False
    return True

#This function returns a list of prime numbers from the given list
def returns_prime_numbers(lis):
    s = []
    for i in range(len(lis)):
        if(is_prime(lis[i])):
            s.append(lis[i])
    return s

#This function generates a list of n random numbers
def generator_lists_numbers(n):
  m = []
  for i in range(n):
    m.append(random.randint(-1000,1000))
  return m

array_size:int = int(input("Enter the number of elements in the list: "))
list_numbers = generator_lists_numbers(array_size)

print(f"list: {list_numbers}")
print(returns_prime_numbers(f"list of prime numbers: {list_numbers}"))
