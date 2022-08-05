#!/usr/bin/env python3
"""
Author : runner <runner@34225f0fefc7>
Date   : 2022-08-05
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import random
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

def scramble(word):
  """Scramble a word"""
  if len(word) <= 3:
    return word
  else:
    start = word[0]
    end = word[-1]
    middle = word[1:-1]
    shuffle = [char for char in middle]
    random.shuffle(shuffle)
    #print(shuffle)
    mid_n = ''.join(shuffle)
    #print(start+mid_n+end)
    return start+mid_n+end
  

def test_scramble():
  """Test scramble"""
  state = random.getstate()
  random.seed(1)
  assert scramble("a") == "a"
  assert scramble("ab") == "ab"
  assert scramble("abc") == "abc"
  assert scramble("abcd") == "acbd"
  assert scramble("abcde") == "acbde"
  assert scramble("abcdef") == "aecbdf"
  assert scramble("abcde'f") == "abcd'ef"
  random.setstate(state)
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    #print(f'{str_arg}')
    
    for line in args.text.splitlines():
      words = []
      for word in splitter.split(line):
        words.append(scramble(word))
      print(''.join(words))

# --------------------------------------------------
if __name__ == '__main__':
    main()
