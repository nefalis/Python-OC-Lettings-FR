Quick Start Guide
=================

1. Make sure all dependencies are installed.

2. Create a .env file for environment variables.

    Create a file named .env in the root directory of the project.

    Add the following environment variables:

    .. code-block:: text

        SECRET_KEY = your_secret_key

    Ensure you replace your_secret_key with your actual configuration.

3. Run migrations to set up the database:

.. code-block:: bash

    python manage.py migrate

4. Start the local server:

.. code-block:: bash

    python manage.py runserver

5. Access the application in your browser at:

.. code-block:: bash

    http://127.0.0.1:8000/

