#Hackerrank
##https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&isFullScreen=true

set1Size = input() #this input was unnecessary
set1 = set(input().split())
set2Size = input()
set2 = set(input().split())
set1,set2 = set1.difference(set2), set2.difference(set1)
finSet = [int(num) for num in list(set1) + list(set2)]
finSet.sort()
for val in finSet:
    print(val)
