#Hackerrank
##https://www.hackerrank.com/challenges/py-set-union/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

engSub = input() #number of english subs
eng_studRol = set(input().split()) #student roll in english sub
frenSub = input()#number of french subs
fren_studRol = set(input().split())#student roll in french sub
totalRoll = eng_studRol.union(fren_studRol)#take the union of both
print(len(totalRoll))#print out total subs

