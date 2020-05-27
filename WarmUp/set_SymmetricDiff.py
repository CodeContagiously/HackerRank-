#Hackerrank
##https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&isFullScreen=true

set1 = set(input())
set2 = set(input())
set1,set2 = set1.difference(set2), set2.difference(set1)
for val in set1:
    if val.isdigit(): print(val)
for val in set2:
    if val.isdigit(): print(val)
