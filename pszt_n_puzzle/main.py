import argparse
import logging

from pszt_n_puzzle.solver import play_game


def main():
    """Runner for this script."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Hello! To solve n_puzzle, enter the appropriate parameters.')
    parser.add_argument('--algorithm-name', type=str, required=True,
                        help='The name of the algorithm we want to use to find '
                             'a solution for the n_puzzle. Choose from bfs or a_star')
    parser.add_argument('--heuristic', type=str, required=False,
                        help='The name of the heuristic we want to use for the A star algorithm. '
                             'Choose from manhattan or misplaces_tiles; if you choose the BFS '
                             'search algorithm, this argument should be bypassed')
    parser.add_argument('--generation-board', action='store_true',
                        help='The argument responsible for generating the board by the program',
                        required=False)
    parser.add_argument('--board-height', type=int, required=False,
                        help='Board height; when loading the board from a file '
                             'this parameter should be omitted - it will be loaded from the file')
    parser.add_argument('--file-path', type=str, required=False,
                        help='Path to the file containing information '
                             'about the board; enter when generating a board from a file')
    parser.add_argument('--save-path', type=str, required=True,
                        help='Path to record steps leading to the solution')
    parser.set_defaults(func=play_game)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
