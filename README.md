# Type Checking in Python with [ty](https://github.com/astral-sh/ty)

Run:

```
uv run ./src/<file>.py
```

#### Basic

| Description   | Syntax  |
| ------------- | ------- |
| String        | `str`   |
| Integer       | `int`   |
| Float/Decimal | `float` |
| Boolean       | `bool`  |
| Bytes         | `bytes` |
| Void/Null     | `None`  |

#### Collection

| Description | Syntax               |
| ----------- | -------------------- |
| List        | `List[T]`            |
| Dictionary  | `Dict[K, V]`         |
| Set         | `Set[T]`             |
| Tuple       | `Tuple[T1, T2, ...]` |
| Iterable    | `Iterable[T]`        |
| Sequence    | `Sequence[T]`        |

#### Other

| Description | Syntax               |
| ----------- | -------------------- |
| Literal     | `Literal[T]`         |
| Union       | `Union[T1, T2, ...]` |
| Optional    | `Optional[T]`        |
| TypedDict   | `TypedDict`          |
| Self        | `Self`               |
| Final       | `Final`              |
| Any         | `Any`                |
