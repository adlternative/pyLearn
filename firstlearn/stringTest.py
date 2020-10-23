# name = "sad"
s = "{name}has{n}messages"


# print(
#     s
# )
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


ss = s.format_map(safesub(vars()))
print(ss)
import sys


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'adl'
n = 31
print(sub('hello {name}'))
print(sub('Your favorite color is {color}'))
print(sub('You have {n} messages.'))

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
# import textwrap, os,curses
# # print(os.get_terminal_size(1).columns)
# # print(textwrap.fill(os.get_terminal_size(1).columns))
# screen = curses.initscr()
# height, width = screen.getmaxyx()
# print(textwrap.fill(s,width))
#
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p=HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
text = 'foo = 23 + 42 * 10'
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
from collections import namedtuple
Token = namedtuple('Token',['type','value'])
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
for tok in generate_tokens(master_pat, 'foo = 42*3+4'):
    print(tok)

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
master_pat = re.compile('|'.join([LE, LT, EQ])) # Correct
import numpy as np
