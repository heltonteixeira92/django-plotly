import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Repository, Commit


class Command(BaseCommand):
    help = 'Generate commits'

    def handle(self, *args, **options):
        user = User.objects.first()
        if not user:
            raise CommandError("Create a superuser before running this command!")

        now = timezone.now()
        previous_year = now - timezone.timedelta(weeks=52)

        # create a repository

        repo = Repository.objects.get_or_create(
            name="The next Facebook",
            user=user
        )[0]

        repo.created = previous_year
        repo.save()

        # generate commits from on year previous.
        # clear any existing first

        Commit.objects.filter(repository=repo).delete()

        delta = now - previous_year

