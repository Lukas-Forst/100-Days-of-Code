#!/usr/bin/env python3
"""
Author : runner <runner@d356d1b96dc6>
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

    parser.add_argument('items',
                        nargs='+',
                        action='append',
                        help='A positional argument')
    parser.add_argument('-s','--sorted',action='store_true')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sorted = args.sorted
    item_list = items[0]
    #print(item_list)
    if sorted:
      item_list.sort(reverse=False)
    output_string = "You are bringing "
    for item in range(len(items[0])):
      if item == len(items[0])-2:
        if len(items[0]) == 2:
          output_string += f"{items[0][item]} and "
        else:
          output_string += f"{items[0][item]}, and "
      elif item == len(items[0])-1:
        output_string += f"{items[0][item]}."
      else:
        output_string += f"{items[0][item]}, "

    print(output_string)
    return output_string

# --------------------------------------------------
if __name__ == '__main__':
    main()
