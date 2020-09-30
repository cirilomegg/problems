# Time complexity: O(V+E)
from queue import Queue


class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class Graph:
    def __init__(self, edges):
        self.dict = {}

        for current in edges:
            if not current.source in self.dict:
                self.dict[current.source] = []

            if not current.destination in self.dict[current.source]:
                self.dict[current.source].append(current.destination)

            if not current.destination in self.dict:
                self.dict[current.destination] = []

            if not current.source in self.dict[current.destination]:
                self.dict[current.destination].append(current.source)

    def print(self):
        for src in self.dict:
            for dest in self.dict[src]:
                print(f"({src} -> {dest}) ", end="")
            print()

    def nodes_length(self):
        return len(self.dict.keys())

    def get(self):
        return self.dict


def dfs(graph, visited, path, start, end):
    if not start in graph.keys():
        return

    path.append(start)
    visited[start] = True

    if start == end:
        print(path)
    else:
        for neighbour in graph[start]:
            if not neighbour in visited:
                dfs(graph, visited, path, neighbour, end)

    visited.pop(start)
    path.pop()


def find_path(graph, start, end):
    visited = {}
    path = []
    dfs(graph, visited, path, start, end)


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(0, 3),
             Edge(2, 0), Edge(2, 1), Edge(1, 3)]

    graph = Graph(edges)
    find_path(graph.get(), 0, 3)
