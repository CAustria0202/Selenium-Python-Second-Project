# Selenium-Python-Second-Project

<h2>Selenium Python Automation for Login Page Testing</h2>

This project demonstrates UI test automation for a sample login page using Selenium WebDriver with Python. The test automates the process of entering correct and incorrect credentials into a login form on the website:

https://trytestingthis.netlify.app/

What It Does:
* Automates the login process by inputting predefined credentials.
* Tests both valid and invalid login attempts.
* Confirms successful login or failure by checking the page content.

Technologies Used:
* Python: The programming language for writing tests.
* Selenium WebDriver: Used for automating browser interactions.
* pytest: A testing framework for running the tests.
* webdriver-manager: Manages the WebDriver binary.

Test Flow:
1. Correct Credentials: The test enters a valid username and password combination and verifies successful login.
2. Incorrect Credentials: The test enters an invalid username or password and checks for failure.

# Requirements

* Python 3.12.3
* pip (24.0) and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/Selenium-Python-Second-Project/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.


# Links
   
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Webdriver Manager for Python](<https://github.com/SergeyPirogov/webdriver_manager>)
   
