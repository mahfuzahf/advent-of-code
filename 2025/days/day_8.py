# imports
from math import sqrt

# Constants
INPUT = '2025/resources/day_8_input.txt'
TEST = '2025/resources/day_8_test.txt'

#############################################################################################################

def get_input(filename):
    
    # read the file
    with open (filename, 'r') as f:
        data = f.read().splitlines()

    # split each line into coords
    string_coords = [item.split(",") for item in data]
    coords = [(int(item[0]), int(item[1]), int(item[2])) for item in string_coords]

    return coords

#############################################################################################################


def init_dist(coords):

    # # number of nodes
    # num_v = len(coords)

    # # need a v x v matrix - all set to 0
    # dist = [[0 for _ in range(num_v)] for _ in range(num_v)]

    # # find the distance between pairs of nodes and store in dist
    # for i in range(num_v):
    #     for j in range(i + 1, num_v):
    #         # get the coords 
    #         coord_i = coords[i]
    #         coord_j = coords[j]
    #         # find the distance 
    #         dist[i][j] = sqrt(((coord_i[0] - coord_j[0])**2) + ((coord_i[1] - coord_j[1])**2) + ((coord_i[2] - coord_j[2])**2))
    #         # set the other one to the same -  do this for full matrix
    #         dist[j][i] = dist[i][j]


    # number of nodes
    num_v = len(coords)

    # dictioanry
    dist = []

    # find the distance between pairs of nodes and store in dist
    for i in range(num_v):
        for j in range(i + 1, num_v):
            # get the coords 
            coord_i = coords[i]
            coord_j = coords[j]
            # find the distance 
            distance = sqrt(((coord_i[0] - coord_j[0])**2) + ((coord_i[1] - coord_j[1])**2) + ((coord_i[2] - coord_j[2])**2))
            # add to dist
            dist.append([distance, i, j])
            

    # sort the distances
    dist = sorted(dist)

    return dist



# distance matrix already initialised
# def floyd_warshall(dist):
#     return


def part_1(dist, rounds, num_v):
    answer = 0

    circuits = []
    circuits.append(set())
    
    nodes = [0 for _ in range(num_v)]

    # for the number of rounds
    for r in range(rounds):

        # pick the shortest distance
        distance = dist.pop(0)

        added = False
        added_to = []

        # for each circuit in circuits, try add it in and if it increases by only 1 then keep it in else move on
        for i, circuit in enumerate(circuits):
            prev_count = len(circuit.copy())
            circuit.add(distance[1])
            circuit.add(distance[2])

            if prev_count == 0:
                added = True
                nodes[distance[1]] = 1
                nodes[distance[2]] = 1
                added_to.append(circuit.copy())

            # if both points added, then there wasn't a conndection so need to remove
            elif len(circuit) - 2 == prev_count:
                
                circuit.remove(distance[1])
                circuit.remove(distance[2])

            else:
                added = True
                nodes[distance[1]] = 1
                nodes[distance[2]] = 1
                added_to.append(circuit.copy())

        # if it wasn't added, create a new set
        if not added:
            nodes[distance[1]] = 1
            nodes[distance[2]] = 1
            circuits.append({distance[1], distance[2]})
        
        # if was added to, but two were, then join the sets together
        if added and (len(added_to) != 1):
            for circuit in circuits:
                if added_to[0] == circuit:
                    circuits.remove(circuit)

            for circuit in circuits:
                if added_to[1] == circuit:
                    circuits.remove(circuit)

            circuits.append(added_to[0] | added_to[1])

    # get the top 3 lengths
    # sort by length
    circuits.sort(key = len, reverse=True)
    
    for i in range(len(nodes)):
        if nodes[i] == 0:
            circuits.append({i})



    answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])



    return answer

#############################################################################################################

input = get_input(INPUT)
# print(input)


print(part_1(init_dist(input), 1000, len(input)))