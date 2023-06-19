from collections import Counter
from itertools import chain
from re import split, sub
from typing import Optional

from pandas import DataFrame, Series
import pandas as pd


def _category_list_per_answer(
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
    return answers


def categories(
    answers: Series,
    synonyms: dict[str, list[str]] = {},
    drop_words: list[str] = [],
    keep_words: Optional[list[str]] = None,
    drop_rows: list[int] = []
) -> Counter[str, int]:

    answers_multi_categories = _category_list_per_answer(answers, synonyms, drop_words, keep_words, drop_rows)

    # Flatten
    words = chain.from_iterable(answers_multi_categories)

    # Count
    counter = Counter(words)

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
    drop_rows: list[int] = [],
) -> DataFrame:

    answers_multi_categories = _category_list_per_answer(answers, synonyms, drop_words, keep_words, drop_rows)
    answers_joined_categories = answers_multi_categories.apply(lambda x: ';'.join(sorted(x)))
    return pd.DataFrame(answers_joined_categories)
