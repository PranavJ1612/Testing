# Any pytest file should start with test_ or end with _test
# pytest method names should always start with test
# Any code should be wrapped inside method.
import pytest


# NOTE-> method name should have sense

# -k => for method name execution ; -s => logs in output ; -v => for more info

# Running pytest from cmd prompt
# 1. Go the pytest path directory
# 2. type "pytest" -> runs test
# 3. type "pytest -v" -> gives detailed info (v is verbose)
# 4. type "pytest -v -s" -> gives console statements (-s does this)


# Running specific file from cmd prompt -> "pytest <file_name.py> -v -s"
# Eg: pytest test_demo2.py -v -s

# Running only those methods that has certain words in method name
# for this use "pytest < -k desired_word > -v"
# eg: pytest -k CreditCard -v -s    => this will run methods having CreditCard in name.

# You can mark (tag) tests with '@pytest.mark.smoke' and then run with '-m <mark_name>'
# eg: pytest -m smoke -v

# Skipping a test => 'pytest.mark.skip'

# Running a test in background but not reporting i.e showing on cmd => '@pytest.mark.xfail'

# Generating html reports for our pytest cases run on cmd prompt -> 'pytest --html=report.html'

# LOGS -> description how ur test case is running,passed or failed.


def test_firstProgram():
    print("Hello getting started!")


@pytest.mark.smoke
def test_first1Program():
    print("Good Morning")


@pytest.mark.skip
def test_CreditCardOne():
    print("BOI credits")
