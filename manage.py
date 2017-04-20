#!/usr/bin/env python
import os
import sys
import time


def wait_for_db(max_attempts=15, seconds_between_attempts=1):
    '''
    Some manage.py commands interact with the database, and we want
    them to be directly callable from `docker-compose run`. However,
    because docker may start the database container at the same time
    as it runs `manage.py`, we potentially face a race condition, and
    the manage.py command may attempt to connect to a database that
    isn't yet ready for connections.
    To alleviate this, we'll just wait for the database before calling
    the manage.py command.
    '''

    from django.db import DEFAULT_DB_ALIAS, connections
    from django.db.utils import OperationalError

    connection = connections[DEFAULT_DB_ALIAS]
    attempts = 0

    while True:
        try:
            connection.ensure_connection()
            break
        except OperationalError as e:
            if attempts >= max_attempts:
                raise e
            attempts += 1
            time.sleep(seconds_between_attempts)
            print("Attempting to connect to database.")

    print("Connection to database established.")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")

    if 'IS_RUNNING_IN_DOCKER' in os.environ:
        wait_for_db()

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
