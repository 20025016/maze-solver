import unittest

from maze import maze_setup
from maze_agent import path_maze_end_goal, research_maze


class TestMazeAgent(unittest.TestCase):
    def setUp(self) -> None:
        maze_filename = ""
        maze_rows_size = 25
        maze_cols_size = 25

        self.maze = maze_setup(maze_filename, maze_rows_size, maze_cols_size)
        self.researched_maze = research_maze(
            self.maze.maze_map, tuple([maze_rows_size, maze_cols_size])
        )

        self.path = path_maze_end_goal(self.researched_maze)

        return super().setUp()

    def test_agent_start_in_correct_location(self):
        keys = list(self.path.keys())

        self.assertEqual(keys[0], tuple([25, 25]))

    def test_agent_finish_at_goal(self):
        keys = list(self.path.keys())
        self.assertEqual(keys[len(keys) - 1], (1, 1))


if __name__ == "__main__":
    unittest.main()
