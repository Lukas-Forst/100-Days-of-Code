#!/usr/bin/env python3
"""
Author : runner <runner@e92dc1c25ac3>
Date   : 2022-08-04
Purpose: Rock the Casbah
"""

import argparse
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()
        #print(args.text)


    return args#parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    words = re.split(r'(\W+)', text)
    for line in args.text.splitlines():
      words = []
      for word in re.split(r'(\W+)', line.rstrip()):
        words.append(fry(word))
      print(''.join(words))


def fry(word):

  if word.lower() == 'you':
    return word[0]+"'all"
  match = re.search('(.+)ing$', word)
  if match:
    first = match.group(1)
    if re.search('[aeiouy]',first.lower()):
      return word[:-1] + "'"
    else:
      return word
  else:
    return word
def test_fry():
  assert fry('you') == "y'all"
  assert fry('You') == "Y'all"
  assert fry('fishing') == "fishin'"
  assert fry('Aching') == "Achin'"
  assert fry('swing') == "swing"
# --------------------------------------------------
if __name__ == '__main__':
    main()
