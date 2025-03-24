import pytest


def test_Hello(setup):
    msg = "hello"
    assert msg == "hi", "Test Failed because strings don't match"


@pytest.mark.xfail
def test_second():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition don't match"


@pytest.mark.smoke
def test_CreditCardSecond():
    print("RBI credits")


# from conftest -> Fixture setup is tied.
def test_fixturedMethod(setup):
    print("I'll execute in between steps of this method.")

