import sys


class Node:

    def __init__(self, data: int):

        self.data = data
        self.edges = dict()  # node val: distance
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


if __name__ == "__main__":

    input = []

    for line in sys.stdin:

        input.append([int(n) for n in str.split(line)])

    n_test = input.pop(0)

    nodes_and_edges = input.pop(0)

    start = input.pop(-1)
