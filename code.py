from typing import List
from collections import deque

class Edge:
    def __init__(self, to: int, rev: int, capacity: int):
        self.to = to
        self.rev = rev
        self.capacity = capacity

class Dinic:
    def __init__(self, n: int):
        self.size = n
        self.graph = [[] for _ in range(n)]
        
    def add_edge(self, fr: int, to: int, capacity: int):
        forward = Edge(to, len(self.graph[to]), capacity)
        backward = Edge(fr, len(self.graph[fr]), 0)
        se