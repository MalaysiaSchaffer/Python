import sys

var1 = []
cases = int(sys.stdin.readline().rstrip())
for i in range(cases):
    var2 = (sys.stdin.readline().rstrip())
    var1.append(var2)
    del var2[0]
    print(var1)
