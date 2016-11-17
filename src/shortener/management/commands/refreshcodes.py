from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refreshes all KirrURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--items', 
            type=int,
            help='Number of shortcodes to refresh (recent first)',
            )

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])