import sys

cases = int(sys.stdin.readline().rstrip())
for i in range(cases):
    smile = (sys.stdin.readline().rstrip().split(" "))
    if smile[0] == "true" and smile[1] == "true":
        print("true")
    elif smile[0] == "false" and smile[1] == "false":
        print("true")
    else:
        print("false")