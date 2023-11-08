from typing import List, TypeVar

T = TypeVar('T')

def linear_search(list: List[T], item: T) -> bool:
    for value in list:
        if value == item:
            return True

    return False

