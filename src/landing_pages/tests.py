from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import LandingPageEntry

User = get_user_model()

class LandingPageEntryTestCase(TestCase):
    fixtures = ["entry-data.json", "users.json"]

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
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), self.inactive_count)

    def test_active(self):
        qs = LandingPageEntry.objects.filter(active=True)
        self.assertTrue(qs.exists())
        self.assertGreaterEqual(qs.count(), 5)

    def test_users_exist(self):
        qs = User.objects.all()
        self.assertTrue(qs.exists())