"""Entry point for the maze solving program."""
import pyamaze

from maze import maze_setup
from maze_agent import path_maze_end_goal, research_maze


def main():
    maze_filename = ""
    maze_rows_size = 20
    maze_cols_size = 20

    maze = maze_setup(maze_filename, maze_rows_size, maze_cols_size)

    researched_maze = research_maze(
        maze.maze_map, tuple([maze_rows_size, maze_cols_size])
    )

    agent = pyamaze.agent(maze, shape="arrow", footprints=True)

    path = path_maze_end_goal(researched_maze)
    maze.tracePath({agent: path})

    maze.run()


if __name__ == "__main__":
    main()
