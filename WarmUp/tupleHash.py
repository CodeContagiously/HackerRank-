#Hackerrank
##https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
