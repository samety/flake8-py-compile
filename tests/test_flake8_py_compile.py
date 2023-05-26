import pytest
from pathlib import Path

from test_data import CODE_WITH_SYNTAX_ERROR
from run_py_compile import PyCompileChecker


@pytest.fixture
def fake_empty_file(tmp_path: Path) -> Path:
    fake_source_file = tmp_path / 'fake_empty_file.py'
    fake_source_file.touch()
    return fake_source_file


@pytest.fixture
def fake_source_file_with_error(tmp_path: Path) -> Path:
    fake_source_file = tmp_path / 'fake_source_file_with_error.py'
    fake_source_file.write_text(CODE_WITH_SYNTAX_ERROR)
    return fake_source_file


def test_py_compile_check_empty_file_expect_no_err(fake_empty_file: Path) -> None:
    checker = PyCompileChecker(None, fake_empty_file)
    errors = list(checker.run())
    assert len(errors) == 0


def test_py_compile_check_faulty_file_expect_error(fake_source_file_with_error: Path) -> None:
    checker = PyCompileChecker(None, fake_source_file_with_error)
    errors = list(checker.run())
    assert len(errors) == 1
    lineno, offset, msg, _ = errors[0]
    assert lineno == 4
    assert offset == 14
    assert msg == 'PYC001 SyntaxError: wildcard makes remaining patterns unreachable'
