#!/usr/bin/env python3
"""
Author : runner <runner@8d8822ca321d>
Date   : 2022-07-21
Purpose: Rock the Casbah
"""

import argparse
import sys

day_one = '\n'.join([
    'On the first day of Christmas,', 'My true love gave to me,',
    'A partridge in a pear tree.'
])

day_two = '\n'.join([
    'On the second day of Christmas,',
    'My true love gave to me,',
    'Two turtle doves,',
    'And a partridge in a pear tree.'
])

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
    0: "A partridge in a pear tree",
    1: "Two turtle doves",
    2 :"Three French hens",
    3 :"Four calling birds",
    4 :"Five gold rings",
    5 :"Six geese a laying",
    6 :"Seven swans a swimming",
    7 :"Eight maids a milking",
    8 :"Nine ladies dancing",
    9 :"Ten lords a leaping",
    10 :"Eleven pipers piping",
    11 :"Twelve drummers drumming"
  }
  
  #day = day-1
  ordinal = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth'] 
  days = []
  
  
  # something here!
  #day = str(day)
  #print(f'On the {ordinal[day]} day of Christmas,')
  #print('My true love gave to me,')
  for i in range(0, day):
    #print(i)
    if i == 0:
      #print(f"{i} is 0?")
      arr = [f'On the {ordinal[i]} day of Christmas,','My true love gave to me,',f'{gifts[i]}.']
      days.append('\n'.join(arr))
    else:
      #print("Test")
      arr_t = [f"On the {ordinal[i]} day of Christmas,","My true love gave to me,"]
      for n in reversed(range(0, i+1)):
        
        if n == 0:
          val = gifts[n]
          
          arr_t.append(f"And {val[0].lower()}{val[1:]}.")
        else:
          arr_t.append(f"{gifts[n]},")
      #arr = '\n'.join(arr_t)
      days.append('\n'.join(arr_t))
      #days.append(arr_t)
  #print(days)
  return '\n\n'.join(days)
    
def test_verse():
  """Test verse
  assert verse(1) == '\n'.join([
  'On the first day of Christmas,', 'My true love gave to me,',
  'A partridge in a pear tree.'
  ])
  assert verse(2) == '\n'.join([
  'On the second day of Christmas,', 'My true love gave to me,',
  'Two turtle doves,', 'And a partridge in a pear tree.'
  ])"""
  assert verse(2) == '\n\n'.join([day_one, day_two])

def main():
    """Make a jazz noise here"""
    args = get_args()
    num = args.num
    file_arg = args.output
    #print(file_arg)
    #if file_arg:
    #  with open(file_arg) as file:
    #    file.write(verse(num))
    print(verse(num), file=file_arg)





# --------------------------------------------------
if __name__ == '__main__':
    main()
