#!/usr/bin/env python3
"""
Author : runner <runner@d7ad95e3af09>
Date   : 2022-07-15
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input file(s)')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    ov_line = 0
    ov_word = 0
    ov_char = 0
    args = get_args()
    for fh in args.file: # ONE LOOP
      print(fh.name)
      data = open(fh.name).read()
      data_ = [line for line in data.split('\n') if line.strip() != '']
      line_count = 0
      if len(data_)
      for line in data_:
        # TWO LOOPS!
        
        print(line)
        
        print(len(data_),len(line.split(' ')), len(data))
       # print(line)

# --------------------------------------------------
if __name__ == '__main__':
    main()
