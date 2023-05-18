from collections import Counter
from itertools import chain
from re import split

from pandas import Series
import pandas as pd


def categories(
    answers: Series,
    synonyms: dict[str, list[str]] = {},
    drop_words: list[str] = [],
    keep_words: list[str] = [],
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

    # Drop words
    for word in drop_words:
        del counter[word]

    # Consolidate synonyms
    for word in list(counter.keys()):
        for preferred, synonyms_ in synonyms.items():
            if word in synonyms_:
                counter[preferred] += counter[word]
                del counter[word]

    # Keep only specified words
    for word in list(counter.keys()):
        if word not in keep_words:
            del counter[word]

    df = pd.DataFrame(
        counter.values(),
        index=counter.keys(),
        columns=['count']
    ).sort_values(by='count', ascending=False)

    total_responses = answers.shape[0]

    df = df.assign(percent=df.apply(lambda x: x/total_responses*100))

    return df
