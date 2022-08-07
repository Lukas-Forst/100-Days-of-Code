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



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #print(args.text)
    vals = []
    for line in args.text.splitlines():
      for word in line.split():
        
        t = ' '.join(word.split())
        t = re.sub('[^A-Za-z0-9]', '', t)
        val = [ord(i) for i in t]
        vals.append(str(sum(val)))
      print(' '.join(vals))
      vals = []
    #word = re.sub('[^A-Za-z0-9 ]', '', args.text)
    #matches = re.findall('[A-Za-z0-9]', word)
    #print(matches)
    #print(word)
    #for i in word:
    #  print(i)
    
  #print(ord("A"))
# --------------------------------------------------
if __name__ == '__main__':
    main()
