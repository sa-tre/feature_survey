from collections import Counter
from itertools import chain
from re import split

from pandas import Series


def categories(
    answers: Series,
    synonms: dict[str, str] = {},
    drop_words: list[str] = [],
    drop_rows: list[int] = []
) -> Counter[str, int]:

    # Drop empty entries
    answers = answers.dropna()

    # drop specified rows
    answers = answers.drop(drop_rows)

    # Split responses into a flat list of words
    words: list[str]
    words = list(chain.from_iterable(split(',|/| ', item) for item in answers))

    # Strip leading and trailing characters from words
    words = [item.strip('.,!“”\'()') for item in words]
    # Drop empty characters
    words = list(filter(lambda x: x != '', words))
    # convert to lower case
    words = [item.lower() for item in list(words)]

    counter = Counter(words)

    # drop words
    for word in drop_words:
        del counter[word]

    return counter