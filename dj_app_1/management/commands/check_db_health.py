"""
database health checker.
"""
import logging

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    this command helps to to check database connection health.
    """
    help = 'Checks the health of configured databases'

    # pylint: disable=unused-argument
    def handle(self, *args, **kwargs):
        """
        the command handler
        """
        for db_alias in connections:
            if db_alias != "default":
                try:
                    with connections[db_alias].cursor() as cursor:
                        cursor.execute("SELECT 1")

                    logger.info("connected successfully %s", db_alias)

                except OperationalError as exc:
                    logger.critical("database %s is down exc %s", db_alias, exc) # noqa
