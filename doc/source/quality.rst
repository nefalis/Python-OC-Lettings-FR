Quality Assurance
=================

This document explains the tools and processes used to ensure the code quality and reliability of the Orange County Lettings project.

Tools used:

- **Flake8**: For code linting and PEP 8 compliance.

- **Pytest**: For automated testing.

- **Coverage**: To measure test coverage.

- **Sentry**: For error monitoring in production.


Code Style with Flake8
-----------------------
To maintain consistent coding standards, the project uses **Flake8** for code linting and style checks.

1. Install Flake8:
    .. code-block:: bash

        pip install flake8

2. Run Flake8:
    .. code-block:: bash

        flake8

Ensure there are no errors before submitting code.


Testing with Pytest
--------------------
All tests are automated using **Pytest**. To verify the integrity of the codebase:

1. Install Pytest:
    .. code-block:: bash

        pip install pytest

2. Run the tests:
    .. code-block:: bash

        pytest


Measuring Test Coverage
------------------------
To ensure sufficient coverage of the codebase, the project uses **Coverage**.

1. Install Coverage:
    .. code-block:: bash

        pip install coverage

2. Run the tests with Coverage:
    .. code-block:: bash

        coverage run -m pytest

3. Generate a coverage report:
    .. code-block:: bash

        coverage report


Error Monitoring with Sentry
-----------------------------
**Sentry** is used to monitor runtime errors and exceptions in production.

Add your Sentry DSN in the `.env` file:
    .. code-block:: bash

        SENTRY_DSN=your-sentry-dsn-url
