import sys
import math

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    asteroid_list = []
    distance_list = []
    A = int(sys.stdin.readline().rstrip())
    for x in range(A):
        asteroid = sys.stdin.readline().rstrip()
        coordinates = asteroid.split(" ")
        
        X = float(coordinates[0])
        Y = float(coordinates[1])
        d = math.sqrt(X**2 + Y**2)
        asteroid_list.append(asteroid)
        distance_list.append(d)
        # print(f'asteroid: {asteroid_list[x]}  --- distance {distance_list[x]}')

    asteroid_distance_list = list(zip(asteroid_list, distance_list)) # Combine the two lists into a list of tuples
    asteroid_distance_list.sort(key=lambda x: x[1]) # Sort the list based on the distance (which is the second element of each tuple)
    asteroid_list, distance_list = zip(*asteroid_distance_list) # Unzip the sorted list back into the two separate lists
    # print(asteroid_list)
    # print(distance_list)
    print(f'asteroid: {asteroid_list[x]}  --- distance {distance_list[x]}')

