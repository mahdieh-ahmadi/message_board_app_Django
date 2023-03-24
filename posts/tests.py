from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

content_test = 'test case data'
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = content_test)

    def test_model_content(self):
        self.assertEqual(self.post.text , content_test)

    def test_Content_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code , 200)

    def test_template_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response , 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, content_test)