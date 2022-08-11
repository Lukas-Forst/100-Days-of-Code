#!/usr/bin/env python3
"""
Author : runner <runner@eea1e1a0442c>
Date   : 2022-08-10
Purpose: Rock the Casbah
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='board',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        choices='XO',
                        metavar='player',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args
  
def format_board(string):
    #string_n = [i+1 for i in range(len(string))]
    strin = ""
    for i in range(len(string)):
      if string[i] == ".":
        strin += str(i+1)
      else:
        strin += string[i]
    #print(strin)
    header = "-------------"
    col1 = f"| {strin[0]} | {strin[1]} | {strin[2]} |"
    col2 = f"| {strin[3]} | {strin[4]} | {strin[5]} |"
    col3 = f"| {strin[6]} | {strin[7]} | {strin[8]} |"
    board_t ='\n'.join([header, col1, header, col2, header,col3,header])
    
    return board_t
def test_board_no_board():
    """makes default board"""
    board = """
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
    """.strip()
    assert format_board('.' * 9) == board

def test_board_with_board():
    """makes board"""
    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
    """.strip()
    assert format_board('...OXX...') == board
def find_winner(board):
  wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]
  #transform board_string
  if "X" not in board and "O" not in board:
    return "No winner."
  if (board.count("X") < 3) and (board.count("O") <3):
    return "No winner."
  x_string = "x"

def test_winning():
    """test winning boards"""
    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
    ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]
    for player in 'XO':
      other_player = 'O' if player == 'X' else 'X'
      for board in wins:
        board = board.replace('P', player)
        dots = [i for i in range(len(board)) if board[i] == '.']
        mut = random.sample(dots, k=2)
        test_board = ''.join([
          other_player if i in mut else board[i]
          for i in range(len(board))
        ])
    assert find_winner(test_board) == player



def test_losing():
    """test losing boards"""
    losing_board = list('XXOO.....')
    for _ in range(10):
      random.shuffle(losing_board)
      assert find_winner(''.join(losing_board)) is None
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board
    player = args.player
    cell = args.cell
    if cell:
      
      board = board[:cell-1] + player + board[cell:]
      #print(board)
    print(format_board(board))
    print(find_winner(board))


# --------------------------------------------------
if __name__ == '__main__':
    main()
