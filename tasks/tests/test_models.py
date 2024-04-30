from django.test import TestCase
from tasks.models import Task, Tag

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")

class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(title="Test Tag")
        self.assertEqual(tag.title, "Test Tag")
