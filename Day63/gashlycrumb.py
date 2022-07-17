#!/usr/bin/env python3
"""
Author : runner <runner@06dfeb4b066d>
Date   : 2022-07-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        nargs='+',
                        help='letter to search')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    letter_dict = dict()
    args = get_args()
    #print(args.file)
    
    for line in args.file:
      letter_dict[line[0]]= line.rstrip()
      #print(line, end='')
    #print(args.letter)
    for letter in args.letter:
      #print(letter)
      val = letter_dict.get(letter.upper())
      if val:
        print(val)
      else:
        print(f'I do not know "{letter}".')
    #print(letter_dict)

# --------------------------------------------------
if __name__ == '__main__':
    main()
