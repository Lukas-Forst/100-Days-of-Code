#!/usr/bin/env python3
"""
Author : runner <runner@0b759feed5f6>
Date   : 2022-07-19
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        type=str,
                        help='A positional argument')

    parser.add_argument('-m',
                        '--mutations',
                        help='A named integer argument',
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='seeed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    mutation = args.mutations
    text = args.positional
    random.seed(args.seed)
    if os.path.isfile(text):
      mut_str = open(text).read().rstrip()
    else:
      mut_str = text
    num_mut = round(len(mut_str)* mutation)
    new_txt = mut_str
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    #print(mutation)
    indexes = random.sample(range(len(mut_str)), num_mut)
    #print(indexes)
    #print(new_txt)
    for i in indexes:
        mut_str = mut_str[:i] + random.choice(alpha.replace(mut_str[i],''))+mut_str[i+1:]
        #mut_str = mut_str[:i] + random.choice(alpha) +mut_str[i+1:]
    print(f'You said: "{new_txt}"')
    print(f'I heard : "{mut_str}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
