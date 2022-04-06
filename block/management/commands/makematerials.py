from django.core.management.base import BaseCommand, CommandError
from block.models import Material

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, *args, **options):
        materials = ["test", "plaster", "roofmembrane"]
        for mat in materials:
            m = Material()
            m.name = mat
            m.save()
            self.stdout.write(f"Saved {mat}")
