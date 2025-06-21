# String
def greet(name: str) -> str:
    return f"Hello, {name}!"


_greet = greet("Code For Real")
print(_greet)


# Integer
def add(a: int, b: int) -> int:
    return a + b


_add = add(1, 2)
print(_add)


# Float
def area_of_circle(radius: float) -> float:
    return 3.14159 * radius**2


_area_of_circle = area_of_circle(2)
print(_area_of_circle)


# Boolean
def is_even(n: int) -> bool:
    return n % 2 == 0


_is_even = is_even(1)
print(_is_even)


# Bytes
def to_bytes(data: str) -> bytes:
    return data.encode("utf-8")


_to_bytes = to_bytes("Code For Real")
print(_to_bytes)


# Void/Null
def log(message: str) -> None:
    print(message)


_log = log("Critical")
