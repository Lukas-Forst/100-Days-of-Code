#!/usr/bin/env python3
"""
Author : runner <runner@643af7ded7d6>
Date   : 2022-07-18
Purpose: Rock the Casbah
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-a',
                        '--adjectives',
                        help='number of adjectives',
                        metavar='int',
                        type=int,
                        default=2)
    parser.add_argument('-n',
                        '--number',
                        help='number of insults',
                        metavar='int',
                        type=int,
                        default=3)
    parser.add_argument('-s',
                        '--seed',
                        help='random seed',
                        metavar='int',
                        type=int,
                        default=None)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

  
    args = get_args()
    random.seed(args.seed)
    parser = argparse.ArgumentParser()

    if args.adjectives < 1:
      parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
      parser.error(f'--number "{args.number}" must be > 0')
    adjectives = """bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed"""
    adjective_list = adjectives.strip().split()

    nouns = """Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward
coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar
lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet
villain worm"""
    noun_list = nouns.strip().split()

    
    for i in range(args.number):
      str = "You "
      sel_adj = random.sample(adjective_list, args.adjectives)
      str += ', '.join(sel_adj)
      sel_nom = random.choice(noun_list)
      str += ' '+sel_nom + "!"
      print(str)
# --------------------------------------------------
if __name__ == '__main__':
    main()
