# E-commerce End-to-End Automation Framework

This project is an End-to-End (E2E) automation testing framework for an e-commerce website using Selenium and Pytest. The framework tests the complete user journey, from login to successfully checking out with a product.

## Prerequisites

To run this project, ensure you have the following installed:

1. Python (Download from Python's official site)

2. Selenium (Install via pip)

3. Pytest (Install via pip)

4. HTML Report Plugin (to generate HTML reports)

## Installation Steps

1. Install Python if you haven’t already.

2. Install the required dependencies:

  > **pip install selenium pytest html-reports**

## Running the Tests

To execute the test suite, run the following command:

  > **pytest -v --html=report.html**

This command will run all the test cases and generate an HTML report (report.html) in the project directory.

## Features

- Full E2E Flow: Automates the process from user login to checkout.

- Pytest Framework: Uses pytest for test execution.

- Selenium WebDriver: Automates browser interactions.

- HTML Reports: Generates detailed test execution reports.

## How to View Reports

After running the tests, open the generated report.html file in a browser to view the test execution details.
