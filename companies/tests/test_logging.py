import logging

logger = logging.getLogger("MY_LOGS")


def function_that_logs_something() -> None:
    try:
        raise ValueError("Raise an exception.")
    except ValueError as e:
        logger.warning(f"Logging warning level {str(e)}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_something()
    assert "Logging warning level Raise an exception." in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info(f"Logging info level")
        assert "Logging info level" in caplog.text
