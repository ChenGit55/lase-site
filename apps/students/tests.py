from django.test import TestCase
from .models import Student
from django.utils.text import slugify
from django.utils import timezone


class StudentTestCase(TestCase):

    def setUp(self):
        self.number_of_students = 5
        for i in range (0, self.number_of_students):
            Student.objects.create(fname = 'melissa', lname = 'carvalho')

    def test_queryset_exsits(self):
        qs = Student.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Student.objects.all()
        self.assertEqual(qs.count(), self.number_of_students)

    def test_slugs(self):
        obj = Student.objects.all().order_by("id").first()
        name = obj.fname
        lname = obj.lname
        birthd = obj.birth_date
        slug = obj.slug
        slugify_instances = f'{name}-{lname}-{birthd}'
        self.assertEqual(slug, slugify_instances)

    def test_unique_slugs(self):
        new_slug = 'melissa-carvalho-2023-03-19'
        obj = Student.objects.all().order_by().first()
        slug = obj.slug
        self.assertNotEqual(new_slug, slug)
