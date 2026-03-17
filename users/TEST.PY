from  django.test import TestCase
from .models import User

class UserTest(TestCase):
    def test_create(self):
        user = User.objects.create(name="Sree",email="test@example.com",age="25")
        self.assertEqual(user.name,"Sree")
        self.assertEqual(user.age,25)