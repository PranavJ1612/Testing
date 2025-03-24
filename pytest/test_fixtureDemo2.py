import pytest


# Instead of tieing multiple methods with fixture that requires fixtures ....
# We can also generalize fixture by creating a class and tieing all test methods to fixture using
# @pytest.mark.usefixtures("fixture_name")

# Note -> The class name should also start as 'Test'.


@pytest.mark.usefixtures("setup")  # all class methods are using fixture  'setup'.
class TestExample:

    def test_fixtureMethod1(self):
        print("I'm running test_fixtureDemo1 code")

    def test_fixtureMethod2(self):
        print("I'm running test_fixtureDemo2 code")

    def test_fixturMethod3(self):
        print("I'm running test_fixtureDemo3 code")

# Now when u need to execute the fixture only once before all test methods execute and
# then directly after all test methods of class finishes execution then we need to pass a argument
# to fixture i.e in conftest -> scope="class"
# Eg. in conftest.py -> @pytest.fixture(scope="class")

# If u don't pass scope to fixture then it will run fixture before/after each and every class method.
