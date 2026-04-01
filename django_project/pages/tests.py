from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomepageTests(SimpleTestCase) :
    def test_url_exists_at_correct_location(self) :
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self) :
        response = self.client.get(reverse("Home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self) :
        response = self.client.get(reverse("Home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self) :
        response = self.client.get(reverse("Home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/About/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self) :
        response = self.client.get(reverse("About"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self) :
        response = self.client.get(reverse("About"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self) :
        response = self.client.get(reverse("About"))
        self.assertContains(response, "<h1>About Page</h1>")
