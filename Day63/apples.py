#!/usr/bin/env python3
"""
Author : runner <runner@692331f9e52a>
Date   : 2022-07-17
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

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='input argument')

    parser.add_argument('-v',
                        '--vowel',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        choices=['a', 'e', 'i','o','u'],
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    #print(vowel, args.text)
    if os.path.isfile(args.text):
      text = open(args.text).read().rstrip()
    else:
      text = args.text
    if text.isupper():
      print(re.sub("[AEIOU]",vowel.upper(),text))
    else:
      print(re.sub("[aeiou]",vowel,text))
    #return text.replace(text, vowel)


# --------------------------------------------------
if __name__ == '__main__':
    main()
