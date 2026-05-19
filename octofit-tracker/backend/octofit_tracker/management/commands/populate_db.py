from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker import models
from djongo import models as djongo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Qui andrà la logica di popolamento
        self.stdout.write(self.style.SUCCESS('Popolamento database avviato (da completare)'))
