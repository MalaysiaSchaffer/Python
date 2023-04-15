import sys

var1 = []
cases = (sys.stdin.readline().rstrip())

# for i in range(int(cases)):
#     var2 = (sys.stdin.readline().rstrip())
#     var1.append(var2)
    
#     var1.sort(reverse=False)
#     for var2 in var1:
#         print(var1)


#for i in range(int(cases)):
for i in range(int(cases)):
    var2 = (sys.stdin.readline().rstrip())


# var2.sort(reverse=True)
for i in var2:
    var1.append(i)
var1.reverse()

