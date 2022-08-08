#!/usr/bin/env python3
"""
Author : runner <runner@8107c3e98d61>
Date   : 2022-08-07
Purpose: Workout of the day
"""

import argparse
import re
import csv
import random
import io
from tabulate import tabulate
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

def read_csv(fh):
  """Read the CSV input"""
  reader = csv.DictReader(fh, delimiter=',')
  
  exercises = []
  for rec in reader:
    
    name, reps = rec['exercise'], rec['reps']
    match = re.match(r'(\d+)-(\d+)', reps)
    #print(match.groups())
    low, high = int(match.groups()[0]), int(match.groups()[1]) # what goes here?
    exercises.append((name, low, high))
  return exercises
def test_read_csv():
  """Test read_csv"""
  text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
  assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    selection = random.sample(exercises, k=args.num)
    if args.easy:
      reps = [(i[0], int(random.randint(i[1],i[2]))//2) for i in selection]
    else:
      reps = [(i[0], random.randint(i[1],i[2])) for i in selection]
    print(tabulate(reps))
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
