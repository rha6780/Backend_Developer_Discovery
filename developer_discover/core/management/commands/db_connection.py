import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting DB Connection")
        connectable = False
        while connectable is False:
            try:
                self.check(databases=["default"])
                connectable = True
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write("DataBase unavailable...")
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS("DataBase is available!"))
