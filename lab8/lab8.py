import random 
import time
import math

def calculate_distance(city_coords, path):
    distance = 0
    num_cities = len(path)
    for i in range(num_cities - 1):
        city1 = path[i]
        city2 = path[i+1]
        x1, y1 = city_coords[city1]
        x2, y2 = city_coords[city2]
        distance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def nearest_neighbor(city_coords):
    num_cities = len(city_coords)

    visited = [False] * num_cities
    start_city = 1
    visited[start_city - 1] = True

    path = [start_city]
    current_city = start_city

    while len(path) < num_cities:
        min_distance = math.inf
        nearest_city = None

        x1, y1 = city_coords[current_city]
        for city_id, coords in city_coords.items():
            if not visited[city_id - 1]:
                x2, y2 = coords
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city_id

        path.append(nearest_city)
        visited[nearest_city - 1] = True
        current_city = nearest_city

    path.append(start_city)
    distance = calculate_distance(city_coords, path)

    return path, distance


city_coords = {}
with open('TSP.txt', 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        city_id = int(line[0])
        x = float(line[1])
        y = float(line[2])
        city_coords[city_id] = (x, y)

path_from_file = [i for i in range(1,len(city_coords)+1)]
start_time = time.time()
distance = calculate_distance(city_coords, path_from_file)
end_time = time.time()
print("time path from file: " + str(end_time-start_time))
print("path from file: ")
print(path_from_file)
print("length of path from file: "+str(distance))


start_time = time.time()
path1, distance1 = nearest_neighbor(city_coords)
end_time=time.time()
print("time nearest_neighbor algorithm: " + str(end_time-start_time))
print("path from nearest_neighbor algorithm: ")
print(path1)
print("length of path from nearest_neighbor: " + str(distance1))
print("improvement: "+str((distance/distance1)*100))
