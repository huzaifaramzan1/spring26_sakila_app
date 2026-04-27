<<<<<<< HEAD
# Authors: Muhammad Huzaifa
# Date: 2026-04-27
# Purpose: Database configuration, timeouts, and health checks for Sakila Flask Application
=======
# Author: Mr John Doe
# Date: 2026-04-27
# Purpose: Health check configuration merged from feature/add-healthcheck
>>>>>>> feature/add-healthcheck

import os

class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """
<<<<<<< HEAD
    # Host kept as sakila-db-server per resolution requirements
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
=======
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
>>>>>>> feature/add-healthcheck
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

<<<<<<< HEAD
    # Both variables included per resolution requirements
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
=======
>>>>>>> feature/add-healthcheck
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')