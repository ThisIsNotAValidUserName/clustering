from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    p_len = len(points)
    center = []

    for item in zip(*points):
        center.append(sum(item) / p_len)

    return center

    raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, data_set):
        clustering[assignment].append(point)

    centers = []
    for key in clustering.keys():
        centers.append(point_avg(clustering[key]))
    return centers

    raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    dist = 0
    for (x, y) in zip(a, b):
        dist += (x - y) ** 2
    return dist ** 0.5

    raise NotImplementedError()


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """

    return random.sample(data_set, k)

    raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):
    dataset = []
    with open(dataset_file) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            new_point = []
            for num in range(0, len(row)):
                new_point.append(int(row[num]))
            dataset.append(new_point)
    return dataset

    raise NotImplementedError()


def cost_function(clustering):
    cost = 0
    for key in clustering.keys():
        points = clustering[key]
        center = point_avg(points)
        for point in points:
            ## distance() calculates Euclidean distance, we want sum of squared distances here.
            cost += distance(center, point) ** 2
    return cost

    raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering
