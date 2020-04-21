# Task
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
#
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
#
# Input Format
#
# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .
#
# Output Format
#
# Print the result of .
#
# Sample Input 0
#
# 2
# 1 2
# Sample Output 0
#
# 3713081631934410656
if __name__ == '__main__':
    t = []
    n = int(input())
    integer_list = list(map(int, input().split()))
    for i in range(n):
        t.append(integer_list[i])
    t=tuple(t)
    print(hash(t))

alt

N = int(input())
T = tuple(int(x) for x in input().split())
print(hash(T))