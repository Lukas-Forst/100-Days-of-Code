#!/usr/bin/env python3
"""
Author : runner <runner@dfbf1b968b39>
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

    parser.add_argument('input',
                        metavar='str',
                        help='A positional input argument')
    parser.add_argument('--side',
                       metavar='str',
                        default="larboard",
                       help='choose a side where the sight be seen')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.input
    side = args.side
    article = "a"
    if word[0].lower() in "aeiou":
      article = "an"
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
