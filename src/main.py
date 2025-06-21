from typing import Set, List, Dict, Tuple, Iterable, Sequence


# List
def total(numbers: List[int]) -> int:
    return sum(numbers)


_total = total([1, 2, 3])
print(_total)


# Dictionary
def invert(d: Dict[str, int]) -> Dict[int, str]:
    return {v: k for k, v in d.items()}


_invert = invert({"one": 1, "two": 2})
print(_invert)


# Set
def unique(values: List[int]) -> Set[int]:
    return set(values)


_unique = unique([1, 2, 3, 1])
print(_unique)


# Tuple
def coordinates() -> Tuple[float, float, str]:
    return (27.7, 85.3, "North")


_coordinates = coordinates()

print(_coordinates)


# Iterable
def reduce_to_sum(items: Iterable[str]) -> int:
    return sum((item if type(item).__name__ == "int" else 0) for item in items)


_reduce_to_sum = reduce_to_sum([1, 2, 3])
print(_reduce_to_sum)


# Sequence
def first_three(items: Sequence[int]) -> Sequence[int]:
    return items[:3]


_first_three = first_three([1, 2, 3, 4, 5])
print(_first_three)
