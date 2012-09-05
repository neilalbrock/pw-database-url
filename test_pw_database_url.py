# coding: utf-8
import os
import unittest

import pw_database_url


class DatabaseTestSuite(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()