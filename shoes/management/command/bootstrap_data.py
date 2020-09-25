from django.core.management.base import BaseCommand, CommandError
from tutorial import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        models.ShoeType.objects.bulk_create(
            [
                models.ShoeType(style = "sneaker"),
                models.ShoeType(style = 'boot'),
                models.ShoeType(style = 'sandal'),
                models.ShoeType(style = 'dress'),
                models.ShoeType(style = 'other')
            ]
        )
        models.ShoeColor.objects.bulk_create(
            [
                models.ShoeColor(color_name="orange"),
                models.ShoeColor(color_name="red"),
                models.ShoeColor(color_name="yellow"),
                models.ShoeColor(color_name="green"),
                models.ShoeColor(color_name="blue"),
                models.ShoeColor(color_name="indigo"),
                models.ShoeColor(color_name="violet"),
                models.ShoeColor(color_name="white"),
                models.ShoeColor(color_name="black")
            ]
        )