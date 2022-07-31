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
  consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])
  pattern = '[' + consonants + ']'
  match = re.match(f'([{consonants}]+)(.+)', 'chair')
  print(match)
  #print(('aeiou' in word.lower()))
  if word == '':
    return ('', '')
  vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
  if any(char in vowels for char in word) == False:
    return (word, '')
  elif word.isdigit():
    return (word, '')
  else:
    matcher = re.match('^[^aeiou]+',word)
    return (word[:matcher.end(0)], word[matcher.end(0):])

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
    print(stemmer(str_arg))

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
