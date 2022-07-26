#!/usr/bin/env python3
"""
Author : runner <runner@8d8822ca321d>
Date   : 2022-07-21
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


    parser.add_argument('-n',
                        '--num',
                        help='number of days',
                        metavar='int',
                        type=int,
                        default=12)
  
    parser.add_argument('-o',
                        '--output',
                        metavar='output',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

  
    args = parser.parse_args()
  
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    if args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return parser.parse_args()


# --------------------------------------------------
def verse(day):
  gifts = {
    1: "A partridge in a pear tree",
    2:"Two turtle doves",
    3 :"Three French hens",
    4 :"Four calling birds",
    5 :"Five gold rings",
    6 :"Six geese a laying",
    7 :"Seven swans a swimming",
    8 :"Eight maids a milking",
    9 :"Nine ladies dancing",
    10 :"Ten lords a leaping",
    11 :"Eleven pipers piping",
    12 :"Twelve drummers drumming"
  }
  #print(day)
  arr_t = []
  ordinal = ['','first','second','third','fourth','fifth','sixth','seventh','eigth','nineth','tenth','eleven','twelve'] # something here!
  #day = str(day)
  arr_t.append(f'On the {ordinal[day]} day of Christmas,')
  arr_t.append('My true love gave to me,')
  if day == 1:
    return f"{gifts[day]}."
  else:
    for n in reversed(range(1, day+1)):
      if n == 1:
        val = gifts[n]
        arr_t.append(f"And {val[0].lower()}{val[1:]}.")
      else:
        arr_t.append(f"{gifts[n]},")
  return '\n'.join(arr_t)
   




def test_verse():
  """Test verse"""
  assert verse(1) == '\n'.join([
  'On the first day of Christmas,', 'My true love gave to me,',
  'A partridge in a pear tree.'
  ])
  assert verse(2) == '\n'.join([
  'On the second day of Christmas,', 'My true love gave to me,',
  'Two turtle doves,', 'And a partridge in a pear tree.'
  ])

def main():
    """Make a jazz noise here"""
    args = get_args()
    num = args.num
    file_arg = args.output
    #if file_arg:
        #with open(file_arg, "w") as file:
          #print(file_arg)
          #text = '\n\n'.join(map(verse, range(args.num,0,-1)))
          #file.write(text)
    for day in range(1, num+1):
      print(verse(day))
    #else:
        #print(text.upper())
        #print('\n\n'.join(map(verse, range(args.num,0,-1))))



# --------------------------------------------------
if __name__ == '__main__':
    main()
