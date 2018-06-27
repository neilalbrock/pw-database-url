# coding: utf-8
import os
import unittest

import pw_database_url


class DatabaseTestSuite(unittest.TestCase):
    def setUp(self):
        # clear env
        for k, v in os.environ.items():
            if k.endswith(pw_database_url.DEFAULT_ENV):
                del os.environ[k]

    def test_truth(self):
        assert True

    def test_postgres_parsing(self):
        url = 'postgres://uf07k1i6d8ia0v:wegauwhgeuioweg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722r2kuvn'
        url = pw_database_url.parse(url)

        assert url['engine'] == 'peewee.PostgresqlDatabase'
        assert url['name'] == 'd8r82722r2kuvn'
        assert url['host'] == 'ec2-107-21-253-135.compute-1.amazonaws.com'
        assert url['user'] == 'uf07k1i6d8ia0v'
        assert url['password'] == 'wegauwhgeuioweg'
        assert url['port'] == 5431

    def test_postgresext_parsing(self):
        url = 'postgresext://uf07k1i6d8ia0v:wegauwhgeuioweg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722r2kuvn'
        url = pw_database_url.parse(url)

        assert url['engine'] == 'playhouse.postgres_ext.PostgresqlExtDatabase'
        assert url['name'] == 'd8r82722r2kuvn'
        assert url['host'] == 'ec2-107-21-253-135.compute-1.amazonaws.com'
        assert url['user'] == 'uf07k1i6d8ia0v'
        assert url['password'] == 'wegauwhgeuioweg'
        assert url['port'] == 5431

    def test_cleardb_parsing(self):
        url = 'mysql://bea6eb025ca0d8:69772142@us-cdbr-east.cleardb.com/heroku_97681db3eff7580?reconnect=true'
        url = pw_database_url.parse(url)

        assert url['engine'] == 'peewee.MySQLDatabase'
        assert url['name'] == 'heroku_97681db3eff7580'
        assert url['host'] == 'us-cdbr-east.cleardb.com'
        assert url['user'] == 'bea6eb025ca0d8'
        assert url['password'] == '69772142'
        assert url['port'] is None

    def test_database_url(self):
        a = pw_database_url.config()
        assert not a

        os.environ['DATABASE_URL'] = 'postgres://uf07k1i6d8ia0v:wegauwhgeuioweg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722r2kuvn'

        url = pw_database_url.config()

        assert url['engine'] == 'peewee.PostgresqlDatabase'
        assert url['name'] == 'd8r82722r2kuvn'
        assert url['host'] == 'ec2-107-21-253-135.compute-1.amazonaws.com'
        assert url['user'] == 'uf07k1i6d8ia0v'
        assert url['password'] == 'wegauwhgeuioweg'
        assert url['port'] == 5431

    def test_multiple_database_parsing(self):
        os.environ.setdefault('DATABASE_URL', 'postgres://user1:pass1@host-1.localhost.com:5432/test_db')
        os.environ.setdefault('DB2_DATABASE_URL', 'mysql://user2:pass2@host-2.localhost.com:3306/test_db')

        databases = pw_database_url.config()

        assert databases['default']['name'] == 'test_db'
        assert databases['default']['host'] == 'host-1.localhost.com'
        assert databases['default']['user'] == 'user1'
        assert databases['default']['password'] == 'pass1'
        assert databases['default']['port'] == 5432

        assert databases['db2']['name'] == 'test_db'
        assert databases['db2']['host'] == 'host-2.localhost.com'
        assert databases['db2']['user'] == 'user2'
        assert databases['db2']['password'] == 'pass2'
        assert databases['db2']['port'] == 3306

if __name__ == '__main__':
    unittest.main()