## Hackerrank problem:
##https://www.hackerrank.com/challenges/no-idea/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

# Enter your code here. Read input from STDIN. Print output to STDOUT
sizesOfarrays = input() #get number of elements in Array and sets
Array = input().split() #get array elements
setA = set(input()) #get elements of sets A & B
setB = set(input())
happiness = 0 #initialise happiness to zero
for element in Array:
    if element in setA:happiness+=1 # increment happiness if element in setA
    elif element in setB:happiness-=1 #decrement happiness if element in setB
print(happiness) #print final value of happiness

'''incomplete'''
