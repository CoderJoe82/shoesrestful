from django.core.management.base import BaseCommand, CommandError
from shoes.models import Manufacturer, Shoe, ShoeColor, ShoeType


class Command(BaseCommand):

    def handle(self, *args, **options):
        ShoeType.objects.bulk_create(
            [
                ShoeType(style="sneaker"),
                ShoeType(style="boot"),
                ShoeType(style="sandal"),
                ShoeType(style="dress"),
                ShoeType(style="other")
            ])
      
        ShoeColor.objects.bulk_create(
            [
                ShoeColor(color_name="red"),
                ShoeColor(color_name="orange"),
                ShoeColor(color_name="yellow"),
                ShoeColor(color_name="green"),
                ShoeColor(color_name="blue"),
                ShoeColor(color_name="indigo"),
                ShoeColor(color_name="violet"),
                ShoeColor(color_name="white"),
                ShoeColor(color_name="black")
            ])

        Manufacturer.objects.bulk_create(
            [
                Manufacturer(name = 'Nike', website = 'https://nike.com'),
                Manufacturer(name = 'Adidas', website = 'https://Adidas.com'),
                Manufacturer(name = 'New Balance', website = 'https://newbalance.com'),
                Manufacturer(name = 'Sketchers', website = 'https://sketchers.com'),
                Manufacturer(name = 'Rebok', website = 'https://Rebok.com'),
            ])