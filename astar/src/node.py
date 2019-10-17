import numpy as np


class Node:

    def __init__(self, city, parent=None, path=[]):

        self.city = city

        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

        self.path = path
        self.successors = []

    def get_successors(self, maze):

        successors = maze.loc[maze[self.city] != 0].index.values.tolist()

        for successor in successors:

            if successor in self.path:
                continue

            successor = Node(successor, parent=self.city,
                             path=self.path+[self.city])

            self.successors.append(successor)

        return self.successors

    def get_path(self):

        return self.path + [self.city]

    def get_cost(self):

        return self.g
