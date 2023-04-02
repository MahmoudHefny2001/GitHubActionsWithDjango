from django.test import TestCase

from .models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title = 'django',
            author = 'django',
            slug = 'django'
        ) 

    def test_post_model(self):
        post = self.post
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), 'django')
