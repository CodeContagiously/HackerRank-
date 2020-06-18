#Hackerrank
##https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    List = []##instantiat list of elements
    for _ in range(N):
        command = input().split()
        method = command[0]
        args = command[1:]
        if method == "print": print(List)
        else: eval("List."+method+"("+",".join(args)+")")
