from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Taco


class StateTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_state = Taco.objects.create(name="Barbacoa", owner=testuser1, meat="Beef", description="delicious.")
        test_state.save()

    def test_tacos_model(self):
        taco = Taco.objects.get(id=1)
        actual_owner = str(taco.owner)
        actual_name = str(taco.name)
        actual_meat = str(taco.meat)
        actual_description = str(taco.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Barbacoa")
        self.assertEqual(actual_meat, "Beef")
        self.assertEqual(actual_description, "Delicious.")

    def test_tacos_model(self):
        test_taco = Taco.objects.get(id=2)
        expected_taco_name = "Barbacoa"
        self.assertEqual(str(test_taco), expected_taco_name)