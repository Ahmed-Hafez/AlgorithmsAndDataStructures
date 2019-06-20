from Queue import *


class UnDirectedGraph:

    def __init__(self, capacity):
        self.capacity = capacity
        self.number_of_edges = 0
        self.number_of_nodes = 0
        self.__adj_list = [None] * self.capacity
        self.visited = [False] * self.capacity

    def add_node(self, node):
        if self.__adj_list[node] is None:
            self.__adj_list[node] = []

    def add_edge(self, from_node, to_node):

        if from_node >= self.capacity or to_node >= self.capacity:
            raise Exception("edge can't be made, node exceeded capacity")

        self.number_of_edges += 1

        if self.__adj_list[from_node] is None:
            self.number_of_nodes += 1
            self.__adj_list[from_node] = [to_node]
            pass
        else:
            self.__adj_list[from_node].append(to_node)
            pass

        if self.__adj_list[to_node] is None:
            self.number_of_nodes += 1
            self.__adj_list[to_node] = [from_node]
            pass
        else:
            self.__adj_list[to_node].append(from_node)
            pass

    def remove_edge(self, from_node, to_node):

        if from_node >= self.capacity or to_node >= self.capacity:
            raise Exception("edge can't be made, node exceeded capacity")

        if self.__adj_list[from_node].__contains__(to_node):
            self.__adj_list[from_node].remove(to_node)
            pass
        else:
            raise Exception("There is no edge between these nodes")

        if self.__adj_list[to_node].__contains__(from_node):
            self.__adj_list[to_node].remove(from_node)
            pass
        else:
            raise Exception("There is no edge between these nodes")

    def dfs(self, node):

        if self.__adj_list[node] is None:
            raise Exception("This node, i.e :", node, " is not inserted in the graph")

        self.visited[node] = True

        for i in self.__adj_list[node]:
            if not self.visited[i]:
                self.dfs(i)
                pass
            pass

    def bfs(self, node):

        if self.__adj_list[node] is None:
            raise Exception("This node, i.e :", node, " is not inserted in the graph")

        self.visited[node] = True

        queue = Queue()
        queue.push(node)

        while not queue.is_empty:
            top = queue.peek()
            queue.pop()
            for i in self.__adj_list[top]:
                if not self.visited[i]:
                    queue.push(i)
                    self.visited[i] = True
                    pass
                pass
            pass

    def connected_components(self):

        n = 0

        for i in range(len(self.__adj_list)):
            if self.__adj_list[i] is not None and not self.visited[i]:
                self.dfs(i)
                n += 1
                pass
            pass

        return n
