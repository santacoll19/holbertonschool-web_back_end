#!/usr/bin/env python3
"""duck typing - element length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of element lengths"""
    return [(i, len(i)) for i in lst]
