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


def find_all_paths(graph, start, end):
    if start == end or not start in graph.keys():
        return

    q = Queue()
    path = [start]
    q.put(path)

    while not q.empty():
        path = q.get()
        last = path[len(path)-1]

        if last == end:
            print(path)
        else:
            for neighbour in graph[last]:
                if not neighbour in path:
                    neighbourPath = path.copy()
                    neighbourPath.append(neighbour)
                    q.put(neighbourPath)


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(0, 2), Edge(0, 3),
             Edge(2, 0), Edge(2, 1), Edge(1, 3)]

    graph = Graph(edges)
    find_all_paths(graph.get(), 1, 3)
