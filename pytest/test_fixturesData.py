import pytest
from BaseClass import LogClass


# NOTE-You should pass the fixture_method as argument to test method(case) when you are returning something from fixture
# Using Datadriven fixture
@pytest.mark.usefixtures("dataLoad")
class TestExample2(LogClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()  # This will get that returned logger by BaseClass
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        for item in dataLoad:
            print(item)


# Parameterized fixtures -> This test case calling param. fixture will execute each time for each data.
# i.e. if 3 ele in list then 3 times.
# You can also call by index number
def test_crossBrowser(crossBrowser):
    # print(crossBrowser)
    print(crossBrowser[1])