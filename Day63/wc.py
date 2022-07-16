#!/usr/bin/env python3
"""
Purpose: Emulate wc (word count)
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
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

    ov_line = 0
    ov_word = 0
    ov_char = 0
    args = get_args()
    for fh in args.file: # ONE LOOP
      word_count=0
      sent_num = 0
      for line in fh:
        if line != "\n":
          word_count += len(line.split(' '))
          #print(line.split(' '))
          sent_num += 1
        else:
          sent_num +=1
      data = open(fh.name).read()
      sent = data.split('\n')
      ov_word += word_count
      if len(data) == 0:
        sent_num=0
        print(f"{sent_num:8}{word_count:8}{len(data):8} {fh.name}")
        return
      print(f"{sent_num:8}{word_count:8}{len(data):8} {fh.name}")
      ov_line += sent_num
      ov_char += len(data)
    if len(args.file) > 1:
        print(f"{ov_line:8}{ov_word:8}{ov_char:8} total")


      

# --------------------------------------------------
if __name__ == '__main__':
    main()
