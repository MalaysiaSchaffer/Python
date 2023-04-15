import sys
import math

cases = int(sys.stdin.readline().rstrip())
#for i in range(cases):
    #input = sys.stdin.readline().rstrip()
    #seperate_numbers=input.split(" ")
sum_list = []
for i in range(cases):
    var1 = (sys.stdin.readline().rstrip())
    var2 = var1.split(" ")
    X = int(var2 [0])
    Y = int(var2 [1])
    A = (X + Y)
    B = (X * Y)
    sum_list.append(A)
    sum_list.append(B)
    print(sum_list)