import logging
import os

from pszt_n_puzzle.board import Board
from pszt_n_puzzle.misc import generate_board, generate_goal_board, animate
from pszt_n_puzzle.state import State
from pszt_n_puzzle.state_search import State_search

logger = logging.getLogger(__name__)


def play_game(args):
    if args.generation_board:
        if args.board_height:
            logger.info("Generating board by the program")
            n = args.board_height
            input_board = generate_board(n * n - 1)
        else:
            raise NameError('The height of the board that the program is to generate has not been entered!')
    else:
        logger.info("Downloading board from a file")
        path = args.file_path
        isFile = os.path.isfile(path)
        if isFile:
            board = []
            with open(path) as file:
                for line in file:
                    board.extend(line.strip().split())
            board = [int(i) for i in board]
            n = board.pop(0)
            input_board = []
            for i in range(0, n):
                tmp = []
                for j in range(0, n):
                    tmp.append(board[i * n + j])
                input_board.append(tmp)
        else:
            raise NameError('The path to the file was not specified or was entered incorrectly!')

    goal = generate_goal_board(n * n - 1)

    if args.algorithm_name == 'bfs':
        board = Board(n, input_board)
        state = State(board, goal, "BFS", 0)
        state.setHeuristicValue()
    elif args.algorithm_name == 'a_star':
        if args.heuristic not in {'manhattan', 'misplaced_tiles'}:
            raise NameError('Heuristic name entered is incorrect!')
        board = Board(n, input_board)
        state = State(board, goal, args.heuristic, 0)
        state.setHeuristicValue()
    else:
        raise NameError('The algorithm name was wrong!')

    if state.isSolvable():
        state_search = State_search(state)
        if args.algorithm_name == 'bfs':
            path = state_search.search_BFS()
        else:
            path = state_search.search_A_star()
        with open(args.save_path, "w") as f:
            counter = 0
            for i in reversed(path):
                counter = counter + 1
                print(i.getBoard())
                print(i.getBoard(), file=f)

            print('Checked states', state_search.getCheckedCount())
            print('Number of empty field moves: ', counter)
            print('Number of empty field moves: ', counter, file=f)
            print("Used process time: {:.4f}s".format(state_search.getUsedTime()))
            print("Used process time: {:.4f}s".format(state_search.getUsedTime()), file=f)
        animate(path, n)
    else:
        raise NameError('There is no solution for this board! Sorry :)')
