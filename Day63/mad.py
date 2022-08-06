#!/usr/bin/env python3
"""Mad Libs"""

import argparse
import os
import sys
import re
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():

  args = get_args()
  text = args.file.read().rstrip()
  #print(text)
    
  matches = re.findall('(<([^<>]+)>)', text)
  #print(matches)
  if matches == []:
    #print(text)
    sys.exit(f'"{args.file.name}" has no placeholders.')
  val_list = []
  if args.inputs:
    for i in args.inputs:
      #print(i)
      text = re.sub(f'(<([^<>]+)>)', i, text, count=1)
    #print(args.inputs)
  else:
    for placeholder, name in matches:
      if re.findall('[aeiou]',name[0].lower()):
        value = input(f'Give me an {name}: ')
        text = re.sub(f'(<([^<>]+)>)', value, text, count=1)
      else:
        value = input(f'Give me a {name}: ')
        text = re.sub(f'(<([^<>]+)>)', value, text, count=1)
  #print(matches)
  print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()
