from typing import Tuple
from collections import Counter
import re

PAT = r'^\W+|\W$'  # leading or trailing non-word characters


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    words = list(map(lambda x: re.sub(PAT, '', x),
                     map(str.casefold, text.split(' '))))
    counts = [(word, Counter([c for c in word if c.isalpha()]))
              for word in words]
    result = max(counts, key=lambda x: x[1].most_common(1)[0][1])
    letter, count = result[1].most_common(1)[0]

    return result[0], letter, count
