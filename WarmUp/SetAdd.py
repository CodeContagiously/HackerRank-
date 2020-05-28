#Hackerrank
##https://www.hackerrank.com/challenges/py-set-add/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


stamps = int(input())#get the total number of stamps 
stampSet = set()#create stamp set
for rep in range(stamps):#for each stamp get the country and add to set.
    country = input()
    stampSet.add(country)
print(len(stampSet)) # print length of set (equivalent to number of distinct stamps)

