from django.test import TestCase

# Create your tests here.
from .models import LandingPageEntry

class LandingPageEntryTestCase(TestCase):
    def setUp(self):
        self.inactive_count = 3
        for i in range(0, self.inactive_count):
            LandingPageEntry.objects.create(
                name='Justin',
                email='abc@gmail.com',
                active=False
            )
        
    
    def test_inactive(self):
        # obj_list = LandingPageEntry.objects.all()
        # inactive_items = [x for x in obj_list if not x.active]
        # assert len(inactive_items) == 2
        qs = LandingPageEntry.objects.filter(active=False)
        # assert qs.count() == 1
        self.assertEqual(qs.count(), self.inactive_count)