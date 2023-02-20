# posts/tests/test_models.py

from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Group, Post

User = get_user_model()

class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост',
            group=cls.group,
        )

    def test_post_model_str_method(self):
        expected_text = self.post.text[:15] + "..."
        self.assertEqual(expected_text, str(self.post))

    def test_group_model_str_method(self):
        expected_title = self.group.title
        self.assertEqual(expected_title, str(self.group))