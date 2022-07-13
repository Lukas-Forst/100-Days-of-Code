#!/usr/bin/env python3
"""
Author : runner <runner@c315d2575d97>
Date   : 2022-07-13
Purpose: Rock the Casbah
"""
import os
import argparse


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

    parser.add_argument('-o',
                        '--output',
                        metavar='output',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.text
    file_arg = args.output

    if os.path.isfile(str_arg):
        text = open(str_arg).read().rstrip()
    else:
        text = str_arg
    if file_arg:
        with open(file_arg, "w") as file:
            # print(file_arg)
            file.write(text.upper())
    else:
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
