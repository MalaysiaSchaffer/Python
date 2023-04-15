import sys
import math
def distance (x,y):
    return(math.sqrt(x*x + y*y))
cases = int(sys.stdin.readline().rstrip())
# for i in range(cases):
#     input = sys.stdin.readline().rstrip()
#     seperate_numbers=input.split(" ")

for i in range(cases):
    asteroid_list = []
    distance_list = []
    A = int(sys.stdin.readline().rstrip())
    for x in range(A):
        asteroid = (sys.stdin.readline().rstrip())
        coordinates = asteroid.split(" ")
        
        X = float(coordinates[0])
        Y = float(coordinates[1])
        X2 = pow(X,2)
        Y2 = pow(Y,2)
        d = math.sqrt(X2 + Y2)
        asteroid_list.append(asteroid)
        distance_list.append(d)
        print(f'asteroid: {asteroid_list[x]}  --- distance {distance_list[x]}')