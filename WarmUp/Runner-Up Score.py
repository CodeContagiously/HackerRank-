#Hackerrank
##https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/forum


n = int(input())
arr = list(map(int, input().split()))
arr.sort()#sort array in ascending order
if arr.count(max(arr))==1: print(arr[-2])#if only a single max val. runer-up is arrr[-2]
else:#else we reduce the size of arr via indexing for runner-up
    firstNum = max(arr)#get current first
    while arr[-1]==firstNum:
        arr=arr[:-1]
    print(arr[-1])
