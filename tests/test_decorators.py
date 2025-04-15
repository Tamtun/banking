import pytest
import logging  # Для работы с caplog
from src.decorators import log


@log()
def sample_function(x: int, y: int) -> int:
    return x + y


@log()
def error_function(x: int, y: int) -> float:
    return x / y


def test_log_success(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO):
        result = sample_function(2, 3)
        assert result == 5

    assert "Start function: sample_function, Inputs: (2, 3), {}" in caplog.text
    assert "sample_function ok, Result: 5" in caplog.text


def test_log_error(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level(logging.INFO):
        with pytest.raises(ZeroDivisionError):
            error_function(2, 0)

    assert "Start function: error_function, Inputs: (2, 0), {}" in caplog.text
    assert "error_function error: ZeroDivisionError, Inputs: (2, 0), {}" in caplog.text


def test_log_to_file(tmp_path: pytest.TempPathFactory) -> None:
    log_file = tmp_path.joinpath("test_log.txt")

    @log(filename=str(log_file))
    def file_function(a: int, b: int) -> int:
        return a * b

    result = file_function(3, 4)
    assert result == 12

    with open(log_file, "r") as f:
        logs = f.read()
        assert "Start function: file_function, Inputs: (3, 4), {}" in logs
        assert "file_function ok, Result: 12" in logs
