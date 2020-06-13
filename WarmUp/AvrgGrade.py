#Hackerrank
##https://www.hackerrank.com/challenges/finding-the-percentage/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average = float(sum(student_marks[query_name]) /len(student_marks[query_name]))
print("%.2f" % average)
