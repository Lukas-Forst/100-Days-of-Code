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
  s1 = '' if num == 1 else 's'
  s2 = '' if num-1 == 1 else 's'
  num_next = 'No more' if num-1 == 0 else num-1
  return '\n'.join([
    f'{num} bottle{s1} of beer on the wall,', f'{num} bottle{s1} of beer,',
'Take one down, pass it around,',f'{num_next} bottle{s2} of beer on the wall!'
])



def test_bottle():
  """Test verse"""
  last_verse = bottle(1)
  assert last_verse == '\n'.join([
'1 bottle of beer on the wall,', '1 bottle of beer,',
'Take one down, pass it around,',
'No more bottles of beer on the wall!',
])
  two_bottles = bottle(2)
  assert two_bottles == '\n'.join(['2 bottles of beer on the wall,', '2 bottles of beer,',
    'Take one down, pass it around,', '1 bottle of beer on the wall!'
])

def main():
    """Make a jazz noise here"""
    args = get_args()
    num = args.num
    print('\n\n'.join(map(bottle, range(args.num,0,-1))))



# --------------------------------------------------
if __name__ == '__main__':
    main()
