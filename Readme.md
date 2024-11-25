## Browser Test Automation Authentication
#### This repo demonstrates two authentication strategies for browser-based applications using Playwright and Python:
-   *Basic Strategy*: Logging in during each test execution.
-   *Efficient Strategy*: Storing and reusing authentication state in the browser context to streamline tests.
#### Requirements:
-   Python
-   [Playwright](https://playwright.dev/python/docs/intro)
-   [pytest](https://docs.pytest.org/en/stable/)
#### Folder Structure:
-   `tests`: Contains the test cases for the authentication strategies.
    -   `test_basic_auth.py`: Contains the test cases for the basic authentication strategy.
    -   `test_efficient_auth.py`: Contains the test cases for the efficient authentication strategy.
-   `pages`: Contains the page objects for the authentication pages.
    -   `index_page.py`: Contains the page object for the index page.
    -   `login_page.py`: Contains the page object for the login page.
    -   `base_page.py`: Contains the base page object for the authentication pages.
-   `config_manager`: Contains the configuration file for the authentication credentials.

#### Run the tests:
1. Clone the repository to your local machine.
2. Install the required dependencies :
```bash
pip install pytest-playwright
pip install pytest-html
playwright install
```
3. Run the tests using `pytest`

```bash
pytest --html=reports/report.html tests/*.py
```