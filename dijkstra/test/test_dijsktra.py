from unittest import TestCase

from dijkstra.src.dijkstra import create_graph, Node, calculate_shortest_distance

input_example = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]


class TestDijsktra(TestCase):
    def test_create_graph_simple(self):

        graph = create_graph(start_val=1, input_list=[[2, 1, 10]])
        self.assertEqual({2: 10}, graph[1].edges)

    def test_create_graph_as_example(self):

        graph = create_graph(start_val=1, input_list=input_example)
        self.assertEqual(4, len(graph.keys()))

    def test_shortest(self):

        expected = [(2, 24), (3, 3), (4, 15)]
        graph = create_graph(start_val=1, input_list=input_example)

        graph_calculated = calculate_shortest_distance(1, graph=graph)

        res = []
        for val in graph_calculated.keys.sort():
            if val != 1:
                res.append((val, graph[val].total_distance))

        self.assertEqual(expected, res)

