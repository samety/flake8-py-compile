# flake8-py-compile

A flake8 plugin for that runs the py_compile module of cpython and checks for all syntax errors during the byte code conversion

For example the code below fails with `PYC001 SyntaxError: name capture 'str' makes remaining patterns unreachable`

```
match 3:
    case str as bla:
        print('str', bla)
    case _:
        print('unknown')
```
