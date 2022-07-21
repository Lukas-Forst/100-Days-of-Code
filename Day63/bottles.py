#!/usr/bin/env python3
"""
Author : runner <runner@8d8822ca321d>
Date   : 2022-07-21
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--num',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()
  
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def bottle(num):
  if num == 0:
    print("No more bottles of beer on the wall!")
  else:
    if num == 1:
      print(f"""{num} bottle of beer on the wall,\n{num} bottle of beer,\nTake one down, pass it around,""")
    else:
      print(f"""{num} bottles of beer on the wall,\n{num} bottles of beer,\nTake one down, pass it around,""")
    
def main():
    """Make a jazz noise here"""
    args = get_args()
    num = args.num
    for i in range(num, -1, -1):
      bottle(i)


# --------------------------------------------------
if __name__ == '__main__':
    main()
