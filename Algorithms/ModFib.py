#Hackerank
#Modified Fibonacci
#Implemented with DP
#time complexity O(n)

def modFib(t1, t2, n):
    if n==1: return t1
    if n==2: return t2
    for num in range(2,n):
        t1, t2 = t2, t1 + (t2*t2)
    return t2


#print(modFib(0,1,5))
