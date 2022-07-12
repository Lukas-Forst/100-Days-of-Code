#!/usr/bin/env python3
"""
Author : runner <runner@d8b7c6be3500>
Date   : 2022-07-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='str',
                        help='A positional argument')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_ = args.number
    in_dict = {
      "1":"9",
      "2":"8",
      "3":"7",
      "4":"6",
      "5":"0",
      "6":"4",
      "7":"3",
      "8":"2",
      "9":"1",
      "0":"5"
    }
    #new_str_ = "Call "
    new_str = ""
    for i in input_:
      if in_dict.get(i):
        new_str+=in_dict.get(i)
      else:
        new_str+=i
    #new_str += " today!"
    #print(input_, new_str)
    print(new_str)

# --------------------------------------------------
if __name__ == '__main__':
    main()
