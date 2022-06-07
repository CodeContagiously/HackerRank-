##
'''
problem:
given n, output the number of primes less than n.
'''


def prime(n):
  if n <= 1:
    return False
  elif (n==2 or n==3):
    return True
  else:
    for i in range(2, n//2+1):
      if(n%i == 0):
        return False
  return True

print(prime(7))



def primeLess(n):
  if n<=1: 
    return 0
  elif(prime(n-1)):
    return 1 + primeLess(n-1)
  return primeLess(n-1) 


print(primeLess(20))
