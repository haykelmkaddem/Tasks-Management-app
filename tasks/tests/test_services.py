from django.test import TestCase
from ..models import Task, Tag
from ..services import create_task, update_task, delete_task

class TaskServiceTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(title="Tag 1")
        self.tag2 = Tag.objects.create(title="Tag 2")

    def test_create_task(self):
        new_task = create_task("New Task", "Description", False, None, None, [self.tag1.id, self.tag2.id])
        self.assertEqual(new_task.title, "New Task")
        self.assertEqual(new_task.description, "Description")
        self.assertFalse(new_task.completed)
        self.assertEqual(new_task.tags.count(), 2)

    def test_update_task(self):
        task = Task.objects.create(title="Task to Update")
        updated_task = update_task(task, "Updated Task", "Updated Description", True, None, None, [self.tag1.id])
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.description, "Updated Description")
        self.assertTrue(updated_task.completed)
        self.assertEqual(updated_task.tags.count(), 1)

    def test_delete_task(self):
        task = Task.objects.create(title="Task to Delete")
        delete_task(task.id)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
