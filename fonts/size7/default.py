from fonts.LetterBlock import LetterBlock
from fonts.exceptions import LetterNotDefined

SIZE = 7
alphabet = {}


def _add(letter, string):
    global alphabet
    letter_str = string.strip()
    assert len(letter_str.split("\n")) == SIZE
    alphabet[letter] = LetterBlock(letter_str)

_add("|", """
x
x
x
x
x
x
x
""")

_add("A", """
xxxxxxxxx
xxx   xxx
xx xxx xx
x       x
x  xxx  x
x  xxx  x
xxxxxxxxx
""")

_add("B", """
xxxxxxxx
x     xx
x  xx  x
x    xxx
x  xx  x
x     xx
xxxxxxxx
""")

_add("C", """
xxxxxxxx
x      x
x  xxxxx
x  xxxxx
x  xxxxx
x      x
xxxxxxxx
""")

_add("D", """
xxxxxxxx
x     xx
x  xx  x
x  xx  x
x  xx  x
x     xx
xxxxxxxx
""")

_add("E", """
xxxxxxxx
x      x
x  xxxxx
x    xxx
x  xxxxx
x      x
xxxxxxxx
""")

_add("F", """
xxxxxxxx
x      x
x  xxxxx
x    xxx
x  xxxxx
x  xxxxx
xxxxxxxx
""")

_add("G", """
xxxxxxxx
x      x
x  xxxxx
x  x   x
x  xx  x
x      x
xxxxxxxx
""")

_add("H", """
xxxxxxxx
x  xx  x
x  xx  x
x      x
x  xx  x
x  xx  x
xxxxxxxx
""")

_add("I", """
xxxx
x  x
x  x
x  x
x  x
x  x
xxxx
""")

_add("J", """
xxxxxx
xxx  x
xxx  x
xxx  x
xxx  x
x    x
xxxxxx
""")

_add("K", """
xxxxxxxx
x  xx  x
x  x  xx
x    xxx
x  x  xx
x  xx  x
xxxxxxxx
""")

_add("L", """
xxxxxxxx
x  xxxxx
x  xxxxx
x  xxxxx
x  xxxxx
x      x
xxxxxxxx
""")

_add("M", """
xxxxxxxxxxxx
x   xxxx   x
x    xx    x
x  x    x  x
x  xx  xx  x
x  xxxxxx  x
xxxxxxxxxxxx
""")

_add("N", """
xxxxxxxxx
x   xx  x
x    x  x
x  x    x
x  xx   x
x  xxx  x
xxxxxxxxx
""")

_add("O", """
xxxxxxxxx
x       x
x  xxx  x
x  xxx  x
x  xxx  x
x       x
xxxxxxxxx
""")

_add("P", """
xxxxxxxx
x     xx
x  xx  x
x     xx
x  xxxxx
x  xxxxx
xxxxxxxx
""")

_add("Q", """
xxxxxxxxxx
x       xx
x  xxx  xx
x  x    xx
x  xx   xx
x        x
xxxxxxx  x
""")

_add("R", """
xxxxxxxxx
x      xx
x  xx   x
x     xxx
x  xx  xx
x  xxx  x
xxxxxxxxx
""")

_add("S", """
xxxxxxxx
x      x
x  xxxxx
x      x
xxxxx  x
x      x
xxxxxxxx
""")

_add("T", """
xxxxxxxx
x      x
xxx  xxx
xxx  xxx
xxx  xxx
xxx  xxx
xxxxxxxx
""")

_add("U", """
xxxxxxxx
x  xx  x
x  xx  x
x  xx  x
x  xx  x
x      x
xxxxxxxx
""")

_add("U", """
xxxxxxxx
x  xx  x
x  xx  x
x  xx  x
xx    xx
xxx  xxx
xxxxxxxx
""")

_add("W", """
xxxxxxxxxx
x  xxxx  x
x  xxxx  x
x  x  x  x
x        x
xx  xx  xx
xxxxxxxxxx
""")

_add("!", """
xxxx
x  x
x  x
x  x
xxxx
x  x
xxxx
""")

_add("1", """
xxxx
x  x
x  x
x  x
x  x
x  x
xxxx
""")

_add("2", """
xxxxxxxx
x      x
xxxxx  x
x      x
x  xxxxx
x      x
xxxxxxxx
""")

_add("3", """
xxxxxxxx
x      x
xxxxx  x
x      x
xxxxx  x
x      x
xxxxxxxx
""")

_add("4", """
xxxxxxxx
x  xx  x
x  xx  x
x      x
xxxxx  x
xxxxx  x
xxxxxxxx
""")


def get_letter(char):
    try:
        return alphabet[char.upper()]
    except KeyError as e:
        raise LetterNotDefined(e)