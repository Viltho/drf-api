from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Movies

# Create your tests here.

class MovieTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Movies.objects.create(name='hello', title=testuser1, description="test ")
        test_thing.save()

    def thigs_model(self):
        thing = Movies.objects.get(id=1)
        actual_name = str(thing.name)
        actual_title= str(thing.title)
        actual_description = str(thing.description)
        self.assertEqual(actual_title,"testuser1")
        self.assertEqual(actual_name,"hello")
        self.assertEqual(actual_description,"test desc ...")

