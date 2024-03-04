from django.conf import settings
from django.core.management.base import BaseCommand

from apps.client.models.client import ClientCategory


class Command(BaseCommand):
    help = 'Create variables for client category model'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start parsing of Dataset...'))
        ClientCategory.objects.all().delete()
        if not ClientCategory.objects.exists():
            client_categories_list = []
            path_to_json = f'{settings.BASE_DIR}/apps/client/management/commands/files/dataset.txt'
            count = 0
            with open(path_to_json, encoding='utf-8') as dataset_file:
                for data in dataset_file.readlines()[1:]:
                    list_data = data.split(',')
                    count += 1
                    client_categories_list.append(
                        ClientCategory(
                            category=list_data[0],
                            first_name=list_data[1],
                            last_name=list_data[2],
                            email=list_data[3],
                            gender=list_data[4],
                            birth_date=list_data[5],
                        )
                    )
                    if count // 100 == 0:
                        self.stdout.write(self.style.SUCCESS(f'Parsed {count} Dataset'))
                ClientCategory.objects.bulk_create(client_categories_list)
        self.stdout.write(self.style.SUCCESS('Done.'))
