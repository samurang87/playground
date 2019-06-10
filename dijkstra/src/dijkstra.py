import sys
from collections import OrderedDict


class Node:
    def __init__(self, data: int):

        self.data = data
        self.edges = dict()  # node val: distance
        self.visited = False
        self.total_distance = None

    def __str__(self):
        return self.data


def create_graph(start_val, input_list):

    graph = dict()
    start_node = Node(data=start_val)
    graph[start_val] = start_node

    for index, edge in enumerate(input_list):
        nodes = sorted(edge[:2])

        for n in nodes:
            if n not in graph.keys():
                graph[n] = Node(data=n)

        if nodes[1] not in graph[nodes[0]].edges.keys():
            graph[nodes[0]].edges[nodes[1]] = edge[-1]
        elif graph[nodes[0]].edges[nodes[1]] > edge[-1]:
            graph[nodes[0]].edges[nodes[1]] = edge[-1]

    return graph


def calculate_shortest_distance(start_val, graph, current=None):

    priority_q = list()

    if current is None:
        current = graph[start_val]
        current.total_distance = 0

    # for each node at the end of the edges
    for edge in current.edges.keys():

        if graph[edge].visited is False:

            # add the distance to the current node to the "distance" property,
            # if the total distance is higher or not None
            distance_from_current = current.edges[edge]
            if (
                graph[edge].total_distance is None
                or graph[edge].total_distance
                > current.total_distance + distance_from_current
            ):
                graph[edge].total_distance = current.total_distance + distance_from_current

            # add the nodes at the end of the edges to the priority list
            priority_q.append(graph[edge])

    current.visited = True

    all_visited = True
    for node in graph.keys():
        if graph[node].visited is False:
            all_visited = False

    if all_visited:
        return graph

    if len(priority_q) > 0:
        # sort by distance
        priority_q.sort(key=lambda x: x.total_distance)

        for node in priority_q:
            calculate_shortest_distance(start_val=start_val, current=node, graph=graph)


if __name__ == "__main__":

    input = []

    for line in sys.stdin:
        input.append([int(n) for n in str.split(line)])

    n_test = input.pop(0)
    nodes_and_edges = input.pop(0)
    start = input.pop(-1)
