"""Maze setup and configuration

Controls the configuration needed for the maze solving to be successful.
"""

import os
from typing import List, Tuple

import pyamaze


def maze_setup(
    maze_filename: str, maze_rows_size: int, maze_cols_size: int
) -> pyamaze.maze:
    """Setups the maze.

    Args:
        maze_filename: The filename of the maze
        maze_rows_size: The number of row cells
        maze_cols_size: The number of column cells

    Returns:
        A maze
    """
    saved_mazes = check_for_saved_mazes()
    if len(saved_mazes) == 0:
        maze = pyamaze.maze(maze_rows_size, maze_cols_size)
        maze.CreateMaze(saveMaze=True)
        return maze
    else:
        return load_maze(
            maze_filename, saved_mazes, maze_rows_size, maze_cols_size
        )


def check_for_saved_mazes() -> List[Tuple[str, int]]:
    """Check for saved mazes, stored in a csv format.

    Returns:
        A list of tuples which contain the filename and the number of cells
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for _, _, files in os.walk(dir_path):
        # Ensures the latest stored maze maps are placed at the top
        files.sort(reverse=True)

        mazes = []
        for filename in files:
            if filename.startswith("maze--") and filename.endswith(".csv"):
                with open(filename, "r", encoding="utf-8") as rf:
                    # Using this get the total of cells
                    lines_num_total = 0
                    for _ in enumerate(rf):
                        lines_num_total += 1

                    # Removing one because the csv has a column heading
                    mazes.append((filename, lines_num_total - 1))

        return mazes

    # No previous mazes exist
    return []


def load_maze(
    maze_filename: str,
    saved_mazes: list[tuple[str, int]],
    maze_rows_size: int,
    maze_cols_size: int,
) -> pyamaze.maze:
    """Loads a saved maze from storage.

    If a maze cannot be found it will create one.

    Args:
        maze_filename: The filename of the maze
        saved_mazes: A list containing the saved mazes
        maze_rows_size: The number of row cells
        maze_cols_size: The number of column cells

    Returns:
        The loaded maze
    """
    # Total cell size of maze
    maze_size = maze_rows_size * maze_cols_size
    # Prepare a maze for matching the provided dimensions
    maze = pyamaze.maze(maze_rows_size, maze_cols_size)
    if maze_filename == "":
        # Match the previously stored mazes to the calculated maze size
        filenames_of_matched_mazes = []
        for m in saved_mazes:
            if m[1] == maze_size:
                filenames_of_matched_mazes.append(m[0])
        if len(filenames_of_matched_mazes) > 0:
            # Load the most recent maze matching the total cell size
            maze.CreateMaze(loadMaze=filenames_of_matched_mazes[0])
        else:
            maze.CreateMaze(saveMaze=True)
    else:
        maze.CreateMaze(loadMaze=maze_filename)
    return maze
