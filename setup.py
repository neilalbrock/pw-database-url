# coding: utf-8
"""
pw-database-url
~~~~~~~~~~~~~~~

This simple Python utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``DATABASE_URL`` environment variable to configure your Peewee ORM application.

All credit goes to Kenneth Reitz for this one, as it's a direct
port of his dj-database-url utility for Django apps.


Usage
-----

Configure your database from ``DATABASE_URL``::

    DATABASE = pw_database_url.config()

Parse an arbitrary Database URL::

    DATABASE = pw_database_url.parse('postgres://...')

Supported databases
-------------------

Support currently exists for PostgreSQL, MySQL and SQLite.

SQLite connects to file based databases. The same URL format is used, omitting
the hostname, and using the "file" portion as the filename of the database.
This has the effect of four slashes being present for an absolute file path:
``sqlite:////full/path/to/your/database/file.sqlite``.


"""

from setuptools import setup

setup(
    name='pw-database-url',
    version='0.1.0',
    url='https://github.com/neilalbrock/pw-database-url',
    license='BSD',
    author='Neil Albrock',
    author_email='neil@atomised.coop',
    description='Use Database URLs in your Peewee ORM application.',
    long_description=__doc__,
    py_modules=['pw_database_url'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
