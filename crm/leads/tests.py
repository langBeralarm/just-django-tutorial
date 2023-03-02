from django.test import TestCase
from django.shortcuts import reverse
from .models import User, UserProfile


class LeadListTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse("leads:lead_list"))
        self.assertEqual(response.status_code, 302)


class LeadCreateTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse("leads:lead_create"))
        self.assertEqual(response.status_code, 302)


class LeadUpdateTest(TestCase):
    def test_get_request(self):
        response = self.client.get(
            reverse(
                "leads:lead_update",
                kwargs={
                    "pk": 1,
                },
            )
        )
        self.assertEqual(response.status_code, 302)


class LeadDeleteTest(TestCase):
    def test_get_request(self):
        response = self.client.get(
            reverse(
                "leads:lead_delete",
                kwargs={
                    "pk": 2,
                },
            )
        )
        self.assertEqual(response.status_code, 302)


class UserProfileTest(TestCase):
    def test_user_post_save_signal(self):
        users = User.objects.all().count()
        self.assertEqual(users, 0)
        user_profiles = UserProfile.objects.all().count()
        self.assertEqual(user_profiles, 0)

        User.objects.create(
            username="Tester",
            first_name="John",
            last_name="Doe",
            email="test@tester.test",
        )

        users = User.objects.all().count()
        self.assertEqual(users, 1)
        user_profiles = UserProfile.objects.all().count()
        self.assertEqual(user_profiles, 1)

        User.objects.all().delete()
        UserProfile.objects.all().delete()
