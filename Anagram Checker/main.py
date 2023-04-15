import sys
def check(var1,var2):
    if var1 == var2:
        print(f"{var1}|{var2} = NOT AN ANAGRAM")
    elif (sorted(var1) == sorted(var2)): 
        print (f"{var1}|{var2} = ANAGRAM")
    else:
        print(f"{var1}|{var2} = NOT AN ANAGRAM")
cases = str(sys.stdin.readline().rstrip())

for i in range(int(cases)):
    var1 = (sys.stdin.readline().rstrip())
    var2 = var1.split("|")
    check(var2[0], var2[1])
            