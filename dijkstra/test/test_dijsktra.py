from unittest import TestCase

from dijkstra.src.dijkstra import create_graph, Node


class TestDijsktra(TestCase):

    def test_create_graph_simple(self):

        graph = create_graph(start_val=1, input_list=[[2, 1, 10]])

        self.assertEqual({2: 10}, graph[1].edges)
mmi