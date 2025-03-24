import pytest

# FIXTURE -> It is a powerful feature that allows you to set up the environment
# or provide dependencies to test functions need to run. help manage common tasks such as
# initializing resources, setting up preconditions, or cleaning up after tests,
# making your tests more modular and reusable.

# We can create fixture using -> '@pytest.fixture'
# the method under this fixture is used for running preconditions and post conditions for ur test functions
# 'yield' keyword makes the statements below wait until ur test function execution is done.

# Note- when u pass fixture function name as argument to test function then only it is attached with fixture.

@pytest.fixture()
def setup():
    print("I'll be executing first")   # code opening browser getting url.
    yield
    print("I'll execute at last")      # code closing browser/deleting cookies.

# Only when u pass a method as argument it is tied up with fixture
def test_fixtureDemo(setup):
    print("I'll execute steps in fixtureDemo")


# when a fixture is required for multiple test files then u can create a file named 'conftest' and
# put all fixture in it and use it directly.
