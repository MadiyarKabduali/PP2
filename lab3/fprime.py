import math 
def filter_primes(numbers):
    return list(filter(lambda x: all(x%i!=0 for i in range(2,int(math.sqrt(x))+1))and x>1,numbers))
nums = [2,3,4,5,10,11,13,17,18,20]
print(filter_primes(nums))