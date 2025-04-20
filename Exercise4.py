import random

#This function compares the sums of consecutive two numbers
#This function returns the largest sum
def greatest_sum_consecutive(lis):
    if(len(lis)<=1):
        return 0
    s = lis[0]+lis[1]
    for i in range(1,len(lis)-1):
        if(s<lis[i]+lis[i+1]):
            s = lis[i]+lis[i+1]
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
print(f"The greatest sum is: {greatest_sum_consecutive(list_numbers)}")