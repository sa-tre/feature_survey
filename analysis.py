from collections import Counter
from itertools import chain
from re import split, sub
from typing import Optional

from pandas import Series
import pandas as pd


def categories(
    answers: Series,
    synonyms: dict[str, list[str]] = {},
    drop_words: list[str] = [],
    keep_words: Optional[list[str]] = None,
    drop_rows: list[int] = []
) -> Counter[str, int]:
    # Drop empty entries
    answers = answers.dropna()

    # Drop specified rows
    answers = answers.drop(drop_rows)

    # Lower case
    answers = answers.apply(lambda x: x.lower())

    # Consolidate synonyms per answer
    for preferred, synonyms_ in synonyms.items():
        for item in synonyms_:
            answers = answers.apply(lambda x: sub(item, preferred, x, count=0))

    # Split words around ',', '/', and ' '
    answers = answers.apply(lambda x: split(',|/| ', x))

    # Strip leading and trailing characters from words
    answers = answers.apply(lambda x: [item.strip('.,!“”\'() ') for item in x])

    # Drop empty characters
    answers = answers.apply(lambda x: filter(lambda y: y != '', x))

    # Keep only unique words per answer (to avoid counting a word multiple
    # times from a single answer)
    answers = answers.apply(lambda x: set(x))

    # Flatten
    words = chain.from_iterable(answers)

    # Count
    counter = Counter(words)

    # Drop words
    for word in drop_words:
        del counter[word]

    # Keep only specified words
    if keep_words:
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


def categories_per_answer(
    answers: Series,
    synonyms: dict[str, list[str]] = {},
    drop_words: list[str] = [],
    keep_words: Optional[list[str]] = None,
    drop_rows: list[int] = []
) -> Series:
    # Fill empty entries
    answers = answers.fillna('')

    # Replace specified drop rows
    answers = answers.replace(drop_rows, '')

    # Lower case
    answers = answers.apply(lambda x: x.lower())

    # Consolidate synonyms per answer
    for preferred, synonyms_ in synonyms.items():
        for item in synonyms_:
            answers = answers.apply(lambda x: sub(item, preferred, x, count=0))

    # Split words around ',', '/', and ' '
    answers = answers.apply(lambda x: split(',|/| ', x))

    # Strip leading and trailing characters from words
    answers = answers.apply(lambda x: [item.strip('.,!“”\'() ') for item in x])

    # Drop empty characters
    answers = answers.apply(lambda x: filter(lambda y: y != '', x))

    # Keep only unique words per answer (to avoid counting a word multiple
    # times from a single answer)
    answers = answers.apply(lambda x: set(x))

    # Drop words
    answers = answers.apply(lambda x: x - set(drop_words))

    # Keep only specified words
    if keep_words:
        answers = answers.apply(lambda x: x & set(keep_words))

    answers = answers.apply(lambda x: ';'.join(x))

    return pd.DataFrame(answers)
