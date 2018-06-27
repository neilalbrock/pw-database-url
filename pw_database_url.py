# coding: utf-8
import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register database schemes in URLs.
urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('postgresql')
urlparse.uses_netloc.append('postgresext')
urlparse.uses_netloc.append('mysql')
urlparse.uses_netloc.append('mysql2')
urlparse.uses_netloc.append('sqlite')

DEFAULT_ENV = 'DATABASE_URL'

SCHEMES = {
    'postgres': 'peewee.PostgresqlDatabase',
    'postgresql': 'peewee.PostgresqlDatabase',
    'postgresext': 'playhouse.postgres_ext.PostgresqlExtDatabase',
    'mysql': 'peewee.MySQLDatabase',
    'mysql2': 'peewee.MySQLDatabase',
    'sqlite': 'peewee.SqliteDatabase'
}


def config(env=DEFAULT_ENV, default=None):
    """Returns configured DATABASE dictionary from DATABASE_URL."""

    config = {}

    for k, v in os.environ.items():
        if k.endswith(env):
            config_key = k.replace('_%s' % env, '')
            config['default' if config_key == env else config_key.lower()] = parse(v)

    if len(config.keys()) == 1 and list(config.keys())[0] == 'default':
        return config['default']

    return config


def parse(url):
    """Parses a database URL."""

    config = {}

    url = urlparse.urlparse(url)

    # Remove query strings.
    path = url.path[1:]
    path = path.split('?', 2)[0]

    # Update with environment configuration.
    config.update({
        'name': path,
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    })

    if url.scheme in SCHEMES:
        config['engine'] = SCHEMES[url.scheme]

    return config
