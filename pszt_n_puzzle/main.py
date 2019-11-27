import argparse
import logging
import os
import numpy as np

from pszt_n_puzzle.board import Board
from pszt_n_puzzle.misc import generate_board, generate_goal_board
from pszt_n_puzzle.state import State
from pszt_n_puzzle.state_search import State_search


def play_game(args):
    
    # input = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
    # goal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
    # n = 3
    #
    # board = Board(n, input)
    # state = State(board, goal, "Misplaces tiles", 0)
    # state.setHeuristicValue()
    #
    # if state.isSolvable():
    #
    #     state_search = State_search(state)
    #     path = state_search.search_A_star()
    #     #print(path)
    #     for i in reversed(path):
    #         i.getBoard().printBoard()
    # else:
    #     exit(1)
    if args.generowanie_planszy_przez_program:
        if args.bok_planszy:
            n = args.bok_planszy
            input_board = generate_board(n*n - 1)
        else:
            raise NameError('Nie wpisano rozmiaru planszy')
    else:
        print("Generowanie planszy z pliku")
        path = args.sciezka_do_pliku
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
                    tmp.append(board[i*n + j])
                input_board.append(tmp)
        else:
            raise NameError('Sciezka do pliku nie zostala podana lub zostala podana blednie')

    goal = generate_goal_board(n * n - 1)

    if args.nazwa_algorytmu == 'bfs':
        board = Board(n, input_board)
        state = State(board, goal, "BFS", 0)
        state.setHeuristicValue()
    elif args.nazwa_algorytmu == 'a_star':
        board = Board(n, input_board)
        state = State(board, goal, args.heurystyka, 0)
        state.setHeuristicValue()
    else:
        raise NameError('Podano zla nazwe algorytmu')

    if state.isSolvable():
        state_search = State_search(state)
        if args.nazwa_algorytmu == 'bfs':
            path = state_search.search_BFS()
            # path = state_search.search_A_star()
        else:
            path = state_search.search_A_star()
        for i in reversed(path):
            i.getBoard().printBoard()
        print('Checked states', state_search.getCheckedCount())
        print("Used process time: {:.4f}s".format(state_search.getUsedTime()))
    else:
        raise NameError('Nie da sie rozegrac gry n_puzzle dla podanej planszy')


def main():
    """Runner dla tego skryptu."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Witaj! Aby solver n_puzzle mogl zostac rozwiazany '
                                                 'wpisz odpowiednie parametry.')
    parser.add_argument('--nazwa-algorytmu', type=str, required=True,
                        help='Nazwa algorytmu, ktorego chcemy uzyc aby znalezc rozwiazanie dla gry n_puzzle:'
                             'bfs lub a_star')
    parser.add_argument('--heurystyka', type=str, required=False,
                        help='Nazwa heurystyki, ktorej chcemy uzyc dla algorytmu A star: '
                             'manhattan lub misplaces_tiles; w przypadku wybrania algorytmu przeszukiwania BFS'
                             'nalezy ten argument pominac')
    parser.add_argument('--generowanie-planszy-przez-program', action='store_true',
                        help='Argument odpowiedzialny za wygenerowanie planszy przez program',
                        required=False)
    parser.add_argument('--bok-planszy', type=int, required=False,
                        help='Ilość kafelkow skladajacych sie na bok planszy; w przypadku wczytywania z pliku '
                             'należy ten parametrem pominac - zostanie on wczytany z pliku')
    parser.add_argument('--sciezka-do-pliku', type=str, required=False,
                        help='Sciezka do pliku, w ktorym znajduja sie informacje o planszy; '
                             'wpisac w przypadku generowania planszy z pliku')
    parser.set_defaults(func=play_game)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
