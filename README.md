# Test automation challenge: Swag Labs

---

## Description:
Python test automation project for [Swag Labs](https://www.saucedemo.com/).

## Rules:
- Use Python 3.7 or newer version.
- Use Selenium to automate [Swag Labs web app](https://www.saucedemo.com/).
- Use virtualenv, although it must be git ignored.
- Add dependencies in a requirements.txt file.
- The project must work with both Google Chrome and Mozilla Firefox.
- The project must run in Windows, macOS and Linux.
- The POM and [BDD](https://behave.readthedocs.io/en/stable/tutorial.html) patterns must be followed.
- One branch per test implementation.
- Develop branch must be used.
- Use a separate Python module/package for project settings purposes.
- Use pyunitreport's HTMLTestRunner for HTML test reports. ([Quick example](https://github.com/gonza56d/pyrty_automation/blob/master/runner.py))

## Encouraged:
- Follow DRY as much as possible.
- Selenium actions wrapper methods with logs are fully encouraged.
- Logs are nice.
- [Python typing](https://docs.python.org/3/library/typing.html) in parameters and return types are nice whenever possible.
- Documentation is always good way to be kind with your teammates and your future self (one-line comments and python docs).
- One fuction/method should do one and only one thing and do it well.
- Environment (Non-test) errors shouldn't pass silently. Imagine the worst and raise exceptions!
- Running tests from the terminal instead of modifying code is always better. Try your own Python file that accepts arguments to run different tests/suites and configurations.
- For configurations files such as different users data you can use [configparser](https://docs.python.org/3/library/configparser.html) with .ini files.

## Useful links:
- [Browsers drivers](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers)
- [BDD quick tutorial](https://behave.readthedocs.io/en/stable/tutorial.html)
