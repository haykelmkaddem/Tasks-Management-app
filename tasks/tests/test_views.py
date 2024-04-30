from django.test import TestCase, Client
from django.urls import reverse
from ..models import Task, Tag

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag1 = Tag.objects.create(title="Tag 1")
        self.tag2 = Tag.objects.create(title="Tag 2")

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/list_task.html')

    def test_task_detail_view(self):
        task = Task.objects.create(title="Test Task")
        response = self.client.get(reverse('task-detail', kwargs={'task_id': task.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_detail.html')

    def test_task_create_view(self):
        response = self.client.post(reverse('task-create'), {'title': 'New Task', 'tags': [self.tag1.id, self.tag2.id]})
        self.assertEqual(response.status_code, 302)  # Redirects to task-list upon success
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update_view(self):
        task = Task.objects.create(title="Task to Update")
        response = self.client.post(reverse('task-update', kwargs={'task_id': task.id}), {'title': 'Updated Task', 'tags': [self.tag1.id]})
        self.assertEqual(response.status_code, 302)  # Redirects to task-list upon success
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.title, 'Updated Task')

    def test_task_delete_view(self):
        task = Task.objects.create(title="Task to Delete")
        response = self.client.post(reverse('task-delete', kwargs={'task_id': task.id}))
        self.assertEqual(response.status_code, 302)  # Redirects to task-list upon success
        self.assertFalse(Task.objects.filter(id=task.id).exists())
