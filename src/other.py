from typing import (
    Union,
    Optional,
    Literal,
    TypedDict,
    Self,
    Final,
    Any,
)


# Literal
def set_theme(theme: Literal["light", "dark"]) -> str:
    return f"Mode set to {theme}"


print(set_theme("light"))


# Union
def stringify(x: Union[int, float, str]) -> str:
    return str(x)


print(stringify(1))
print(stringify(1.2))
print(stringify("1"))


# Optional
def save_gender(gender: Optional[Literal["Male", "Female", "Others"]] = None):
    if gender is not None:
        # Save
        pass
    # Do nothing


print(save_gender("Male"))
print(save_gender())


# Typed Dict
class User(TypedDict):
    id: int
    name: str


def greet_user(user: User) -> str:
    return f"Hello, {user['name']}!"


print(greet_user(User({"id": "123", "name": "Code For Real"})))


# Self


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> Self:
        self.count += 1
        return self


counter = Counter()
_counter = counter.increment()
print(_counter.count)

# Final
PI: Final[float] = 3.14


# Any
def debug_output(data: Any) -> None:
    print("DEBUG:", data)


debug_output("hello")
debug_output(1)
