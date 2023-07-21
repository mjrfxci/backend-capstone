from django.test import TestCase
from .models import MenuItem

# Create your tests here.
class MenuTest(TestCase):
    @classmethod
    def Menu(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item, "IceCream : 80")