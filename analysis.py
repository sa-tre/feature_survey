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
    return Counter(chain.from_iterable(split(',| ', item) for item in answers))
