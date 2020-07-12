from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Blogger, Blog

class BloggerListViewTest(SimpleTestCase):           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/bloggers/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bloggers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogger_list.html')

class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a blogger
        name = 'awesome_blogger'
        bio = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua."""
        blogger = Blogger.objects.create(name=name, bio=bio)
        
        # Create 8 blog Blogs for pagination tests
        number_of_blogs = 8

        for blog_id in range(number_of_blogs):
            title = f"Blog {blog_id}"
            description = f"""Lorem ipsum {blog_id} dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat."""
                
            Blog.objects.create(title=title, description=description)
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')
        
    def test_blog_list_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 5)

    def test_lists_all_blogs(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('blogs')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 3)