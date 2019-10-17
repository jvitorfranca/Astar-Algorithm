import numpy as np

from astar.src import Node


def astar(maze, heuristic, start, end):

    start = Node(start, None)

    end = Node(end, None)

    open_list = []

    closed_list = []

    open_list.append(start)

    while len(open_list) > 0:

        open_list = sorted(open_list, key=lambda x: x.f)

        q = open_list.pop(0)

        if q.city == end.city:

            return q

        successors = q.get_successors(maze)

        for successor in successors:

            successor.g = q.g + maze[q.city][successor.city]

            successor.h = heuristic[successor.city][end.city]

            successor.f = successor.g + successor.h

            open_list.append(successor)

        closed_list.append(q)
