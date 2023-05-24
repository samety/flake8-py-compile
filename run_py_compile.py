import ast
import py_compile
from typing import Iterator


class PyCompileChecker:
    name = 'flake8-py-compile'
    version = '0.1.0'

    def __init__(self, tree: ast.Module, filename: str) -> None:
        self.filename = filename

    def run(self) -> Iterator[tuple[int, int, str, type]]:
        try:
            py_compile.compile(self.filename, doraise=True)
        except py_compile.PyCompileError as err:
            underlying_error = err.exc_value
            if not isinstance(underlying_error, SyntaxError):
                raise
            msg = f'PYC001 SyntaxError: {underlying_error.args[0]}'
            yield underlying_error.lineno, underlying_error.offset, msg, type(self)
