import random
from time import sleep

def random_matrix_gen(n):
    mat = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    return mat

def find_nearest_unmapped(matrix, current_position, mapped_tiles):
    min_distance = float('inf')
    nearest_position = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and (i, j) not in mapped_tiles:
                distance = abs(i - current_position[0]) + abs(j - current_position[1])
                if distance < min_distance:
                    min_distance = distance
                    nearest_position = (i, j)

    return nearest_position

def map_3x3_around_position(matrix, position):
    for i in range(position[0] - 1, position[0] + 2):
        for j in range(position[1] - 1, position[1] + 2):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                matrix[i][j] = 1

def robot_mapping(matrix):
    mapped_tiles = set()
    current_position = (0, 0)

    while True:
        nearest_position = find_nearest_unmapped(matrix, current_position, mapped_tiles)
        if nearest_position is None:
            break

        map_3x3_around_position(matrix, nearest_position)
        print_matrix(matrix)
        mapped_tiles.add(nearest_position)
        current_position = nearest_position
        sleep(0.5)

def print_matrix(mat: list[list[int]]):
    for row in mat:
        print(row)
    print()

matrix = random_matrix_gen(10)

robot_mapping(matrix)