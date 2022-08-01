#!/usr/bin/env python3


import argparse
import sys
import re
import string as s
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', metavar='word', help='A word to rhyme')




    return parser.parse_args()
def stemmer(word):
  """Return leading consonants (if any), and 'stem' of word"""
  
  #print(('aeiou' in word.lower()))
  if word == '':
    return ('', '')
  #vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
  #if any(char in vowels for char in word) == False:
    #print(word)
    #return (word.lower(), '')
  elif word.isdigit():
    return (word, '')
  else:
    #print(word)
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])
    pattern = '[' + consonants + ']'
    matcher_2 = re.match(f'([{consonants}]+)?([aeiou])(.*)', word.lower(), re.IGNORECASE)#
    #print(matcher_2.group(0),matcher_2.group(1), matcher_2.group(2))
    if matcher_2:
      p1 = matcher_2.group(1) or ''
      p2 = matcher_2.group(2) or ''
      p3 = matcher_2.group(3) or ''
      return (p1, p2 + p3)
    else:
      return (word, '')


def test_stemmer():
  """ Test stemmer """
  assert stemmer('') == ('', '')
  assert stemmer('cake') == ('c', 'ake')
  assert stemmer('chair') == ('ch', 'air')
  assert stemmer('APPLE') == ('', 'apple')
  assert stemmer('RDNZL') == ('rdnzl', '')
  assert stemmer('123') == ('123', '')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.word
    tup = stemmer(str_arg)
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])
    pattern = '[' + consonants + ']'
    match = re.match(f'([{consonants}]+)?(.+)', 'rdnzl')
    consonants_a = ["bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gl", "gr", "pl",         "pr", "sc", "sh", "sk", "sl", "sm", "sn", "sp", "st","sw", "th", "tr", "tw", "thw",       "wh", "wr", "sch", "scr", "shr", "sph", "spl", "spr", "squ", "str", "thr"]
    consonants_n = [c for c in s.ascii_lowercase if c not in 'aeiou']
    consonants_n.extend(consonants_a)
    #print(consonants_n)
    consonants_n.sort()
    #print(tup)
    if tup[0] != '' and tup[1] != '':
      for i in consonants_n:
        if tup[0] != '':
          if i+tup[1] != str_arg.lower():
            print(i+tup[1])
    elif tup[0] == '' and tup[1] != '':
      for i in consonants_n:
        print(i+tup[1])
    else:
      print(f'Cannot rhyme "{str_arg}"')
    #print(match.groups())

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
