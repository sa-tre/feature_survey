from collections import Counter
from itertools import chain
from re import split
from typing import Optional


def categories(
    answers: list[str],
    synonms: Optional[dict[str, str]] = None,
    drop_words: Optional[list[str]] = None,
    drop_rows: Optional[list[int]] = None
) -> Counter[str, int]:

    # Split responses into a flat list of words
    words = chain.from_iterable(split(',|/| ', item) for item in answers)

    # Strip leading and trailing characters from words
    words = [item.strip('.,!“”\'()') for item in words]
    # Drop empty characters
    words = list(filter(lambda x: x != '', words))
    # convert to lower case
    words = [item.lower() for item in list(words)]

    return Counter(words)
