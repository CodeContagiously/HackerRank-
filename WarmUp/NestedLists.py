#Hackerrank
##https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen


students = [] #instantiate list for student info: name and grade
maxGrade = 0.0
for student in range(int(input())):
    name = input() #get name of student
    score = float(input()) #get student grade
    if maxGrade < score: maxGrade = score
    info = [name, score] #create a list of student info
    students.append(info)#add info of student to student List

''' take another approach ''''
