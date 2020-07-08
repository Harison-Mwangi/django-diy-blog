from django.test import TestCase
from blog.models import Blogger

class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        name = 'awesome_blogger'
        bio = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat."""
        Blogger.objects.create(name=name, bio=bio)

    def test_name_label(self):
        blogger= Blogger.objects.get(id=1)
        field_label = Blogger._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_bio_label(self):
        blogger= Blogger.objects.get(id=1)
        field_label = Blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_name_max_length(self):
        blogger= Blogger.objects.get(id=1)
        max_length = Blogger._meta.get_field('name').max_length
        self.assertEquals(max_length, 25)

    def test_bio_max_length(self):
        blogger= Blogger.objects.get(id=1)
        max_length = Blogger._meta.get_field('bio').max_length
        self.assertEquals(max_length, 250)

    # custom class methods
    def test_blogger_name_is_name(self):
        blogger= Blogger.objects.get(id=1)
        expected_object_name = Blogger.name
        self.assertEquals(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger= Blogger.objects.get(id=1)
        self.assertEquals(Blogger.get_absolute_url(), '/catalog/blogger/1')