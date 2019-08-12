from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "test@carousell.com"
        password = "1234567"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@carousell.COM"
        user = get_user_model().objects.create_user(
            email, "1234567"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@carousell.com",
            "1234567"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
