# flake8-py-compile

A flake8 plugin for that runs the py_compile module of cpython and checks for all syntax errors during the byte code conversion

For example the code below fails with `PYC001 SyntaxError: wildcard makes remaining patterns unreachable`

```
def boo(x: Any) -> None:
    match x:
        case _:
            pass
        case int() as x:
            print('x=', x)
```
