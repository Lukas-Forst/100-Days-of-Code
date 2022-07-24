#!/usr/bin/env python3
"""
Author : runner <runner@310e3d7ee5b0>
Date   : 2022-07-23
Purpose: Rock the Casbah
"""

import argparse
import random
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-s',
                        '--seed',
                        help='random seed',
                        metavar='int',
                        type=int,
                        default=0)

    args = parser.parse_args()

    if os.path.isfile(args.positional):
        args.positional = open(args.positional).read().rstrip()

    return args

def choose(string):
  #print(random.seed())
  val = string.upper() if random.choice([0,1]) else string.lower()
  return val

def test_choose():
  state = random.getstate()
  random.seed(1)
  assert choose('a') == 'a'
  assert choose('b') == 'b'
  assert choose('c') == 'C'
  assert choose('d') == 'd'
  random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional
    #print(pos_arg)
    random.seed(args.seed)
    val = ''.join(map(choose,pos_arg))
    print(val)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
