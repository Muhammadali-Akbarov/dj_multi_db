"""
the storage settings module.
"""
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


class DatabaseRouter:
    """
    database rounter between mysql and psql
    """
    psql_model = [
        "payment"
    ]

    mysql_models = [
        "order"
    ]

    def db_for_read(self, model):
        """
        getting read access.
        """
        engine = "unknown"

        # pylint: disable=protected-access
        if model._meta.model_name in self.psql_model:
            engine = 'psql'

        if model._meta.model_name in self.mysql_models:
            engine = 'mysql'

        return engine

    def db_for_write(self, model):
        """
        getting write acccess.
        """
        # pylint: disable=protected-access
        engine = "unknown"

        # pylint: disable=protected-access
        if model._meta.model_name in self.psql_model:
            engine = 'psql'

        if model._meta.model_name in self.mysql_models:
            engine = 'mysql'

        return engine


DATABASES = {
    "default": {},
    "psql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "psql_dj_multi_db",
        "USER": "psql_dj_multi_db",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    },
    "mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mysql_dj_multi_db",
        "USER": "mysql_dj_multi_db",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    },
}

DATABASE_ROUTERS = [
    'dj_multi_db.settings.storage.DatabaseRouter'
]
