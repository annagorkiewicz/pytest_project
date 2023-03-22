import pytest


@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_be_skipped_if_fails() -> None:
    assert 1 == 2


def raise_custom_exception() -> None:
    raise ValueError("Raises custom exception.")


def test_raise_custom_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_custom_exception()
    assert "Raises custom exception." == str(e.value)
