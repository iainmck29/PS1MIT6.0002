###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1


def load_cows(filename):
    cows = {}
    with open(filename) as f:
        for line in f:
            val = line.strip().split(',')
            cows[val[0]] = val[1]
    return cows


# load_cows('ps1_cow_data.txt')

# Problem 2


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
    sorted_cows = dict(
        sorted(cows.items(), key=lambda item: item[1], reverse=True))
    journeys = []
    current_weight = 0
    current_journey = []

    for cow in sorted_cows.items():
        current_weight += int(cow[1])
        if current_weight >= limit:
            journeys.append(current_journey)
            current_journey = []
            current_weight = 0
            current_journey.append(cow[0])
            current_weight += int(cow[1])

        else:
            current_journey.append(cow[0])
            current_weight += int(cow[1])

    # print(journeys)
    return journeys


cows = load_cows('ps1_cow_data.txt')
greedy_cow_transport(cows)

# Problem 3


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
    result = []
    for partition in get_partitions(cows):
        check_weight = False
        for i in partition:
            current_weight = 0
            for cow in i:
                current_weight += int(cows[cow])
                if current_weight >= limit:
                    check_weight = True
                    break
        if check_weight:
            continue
        elif len(result) == 0 or len(partition) < len(result):
            result = partition
    return result


# Problem 4
# brute_force_cow_transport(cows)


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
    start = time.time()
    print(len(greedy_cow_transport(cows)))
    end = time.time()
    print(end - start)

    start2 = time.time()
    print(len(brute_force_cow_transport(cows)))
    end2 = time.time()
    print(end2 - start2)


compare_cow_transport_algorithms()
