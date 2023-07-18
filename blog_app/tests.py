from django.contrib.auth import get_user_model
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse
import os

from .models import Blog


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<title>Blog</title>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)


class BlogTests(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.user = get_user_model().objects.create(
            username="testuser", email="test@email.com"
        )
        cls.user.set_password("test@123")
        cls.user.save()

        cls.blog = Blog.objects.create(
            title="Hello Test", body="hello world", author=cls.user
        )

    def test_blog_content(self):
        self.assertEqual(self.blog.title, "Hello Test")
        self.assertEqual(str(self.blog), "Hello Test")
        self.assertEqual(self.blog.body, "hello world")
        self.assertEqual(self.blog.author.username, "testuser")
        self.assertEqual(self.blog.get_absolute_url(), "/blog/1/")

    def test_url_redirects_at_signup_or_login_location_listview(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 302)

    def test_url_available_by_name(self):
        self.client = Client()
        self.client.post(
            "/accounts/login/",
            {
                "username": os.environ.get("username"),
                "password": os.environ.get("password"),
            },
        )

        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)
