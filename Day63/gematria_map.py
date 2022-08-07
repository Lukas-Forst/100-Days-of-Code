#!/usr/bin/env python3
"""
Author : runner <runner@ba5392ab8802>
Date   : 2022-08-07
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
                        help='Input string or file')
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

def word2num(word):
  
  return str(sum(map(ord, re.sub('[^A-Za-z0-9 ]', '', word))))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():           
      print(' '.join(map(word2num, line.split()))) 


# --------------------------------------------------
if __name__ == '__main__':
    main()
