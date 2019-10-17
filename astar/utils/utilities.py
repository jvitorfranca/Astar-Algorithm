import pandas as pd
import numpy as np


def get_dataframe(file):

    df = pd.read_excel(file,
                       skiprows=[0, 1], index_col=0)

    df.fillna(0, inplace=True)

    return df


def get_maze(dataframe):

    maze = dataframe.values

    for i in range(0, len(maze)):
        for j in range(0, len(maze)):
            maze[i][j] = maze[j][i]

    maze = pd.DataFrame(maze, index=list(dataframe.columns),
                        columns=list(dataframe.columns))

    return maze


def get_heuristic(dataframe):

    heuristic = dataframe.values

    for i in range(0, len(heuristic)):
        for j in range(0, len(heuristic)):
            heuristic[j][i] = heuristic[i][j]

    heuristic = pd.DataFrame(heuristic, index=list(
        dataframe.columns), columns=list(dataframe.columns))

    return heuristic


def check_city(maze, start, end):

    if start in maze.index.values.tolist():

        if end in maze.index.values.tolist():

            return True

    return False
