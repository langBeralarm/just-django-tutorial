from django.test import TestCase
from django.shortcuts import reverse


class LeadListTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse("leads:lead_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_list.html")


class LeadCreateTest(TestCase):
    def test_get_request(self):
        response = self.client.get(reverse("leads:lead_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_create.html")


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
        self.assertEqual(response.status_code, 404)


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
        self.assertEqual(response.status_code, 404)
