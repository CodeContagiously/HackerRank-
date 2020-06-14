#Hackerrank
##https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen


if __name__ == '__main__':
    List = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        List.append([name, score])
    Scos = [x[1] for x in List] ## create list of scores only
    Scos.sort()
    secMin, Students = Scos[1], [] #get second minimum after sorting list and instantiate stdent list
    for stdnt in List: 
        if stdnt[1] == secMin: Students.append(stdnt[0])##add name of student with secMin score in list
    Students.sort()
    print(*Students, sep="\n")
