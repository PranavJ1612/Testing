import pytest


# This file contains fixture that r available to all test function files (test cases) wo repeating code in each file.
# For this file name should be strictly 'conftest.py'.


# used this fixture in test_demo2.py
@pytest.fixture(scope="class")
def setup():
    print("I'll be executing first")  # code opening browser getting url.
    yield
    print("I'll execute at last")  # code closing browser/deleting cookies.


# Datadriven Fixture
@pytest.fixture()
def dataLoad():
    print("User profile  data is being created")
    return ["Pranav", "Jagdale", "testpranav100@gmail.com"]


# Parametrized Fixture -
# For having param fixtures we need u use params= ['values...'] in fixture.
# For using these params value we use 'request' keyword in crossBrowser and for returning it use 'request.param'
@pytest.fixture(params=[("chrome", "pranav", "jagdale"),("Firefox", "prajwal"),("IE", "test")])
def crossBrowser(request):
    return request.param