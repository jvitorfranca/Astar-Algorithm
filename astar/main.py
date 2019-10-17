import argparse
import sys

from astar.src import Node
from astar.src import astar
from astar.utils import (
    get_dataframe,
    get_heuristic,
    get_maze,
    check_city
)


def main(args):

    dataframe = get_dataframe(args.file)

    maze = get_maze(dataframe)

    if check_city(maze, args.start, args.end):

        heuristic = get_heuristic(dataframe)

        node = astar(maze, heuristic, args.start, args.end)

        print(' -> '.join(node.get_path()))

        print('COST: {0}'.format(node.get_cost()))

    else:

        print('You must insert city name as it is in the csv file.')

        sys.exit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A* Algorithm")

    parser.add_argument('--file', type=str,
                        default='data/distancias capitais.xlsx')
    parser.add_argument('--start', type=str)
    parser.add_argument('--end', type=str)

    main(parser.parse_args())
