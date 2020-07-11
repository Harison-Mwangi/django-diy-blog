from django.test import TestCase
from blog.models import Blogger, Post, Comment
from datetime import date

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
        field_label = Blogger._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_bio_label(self):
        field_label = Blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_name_max_length(self):
        max_length = Blogger._meta.get_field('name').max_length
        self.assertEquals(max_length, 25)

    def test_bio_max_length(self):
        max_length = Blogger._meta.get_field('bio').max_length
        self.assertEquals(max_length, 250)

    # custom class methods
    def test_blogger_name_is_name(self):        
        blogger= Blogger.objects.get(id=1)
        expected_object_name = blogger.name
        self.assertEquals(expected_object_name, str(blogger))

    # def test_get_absolute_url(self):
    #     blogger= Blogger.objects.get(id=1)
    #     self.assertEquals(blogger.get_absolute_url(), '/blog/blogger/1')

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        title = "My first blog"
        description = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        Post.objects.create(title=title, description=description)

    # labels
    def test_title_label(self):
        field_label = Post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_author_label(self):
        field_label = Post._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_date_posted_label(self):
        field_label = Post._meta.get_field('date_posted').verbose_name
        self.assertEquals(field_label, 'date posted')
    
    def test_last_edit_label(self):
        field_label = Post._meta.get_field('last_edit').verbose_name
        self.assertEquals(field_label, 'last edit')

    def test_description_label(self):
        field_label = Post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    # max length
    def test_title_max_length(self):
        max_length = Post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        max_length = Post._meta.get_field('description').max_length
        self.assertEquals(max_length, 4000)

    # custom class methods
    def test_post_name_is_title(self):        
        post= Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name, str(post))

    # def test_get_absolute_url(self):
    #     post= Post.objects.get(id=1)
    #     self.assertEquals(post.get_absolute_url(), '/blog/1')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        description = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
            proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        Comment.objects.create(description=description)

    # labels
    def test_blog_label(self):
        field_label = Comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label, 'blog')

    def test_author_label(self):
        field_label = Comment._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_date_posted_label(self):
        field_label = Post._meta.get_field('date_posted').verbose_name
        self.assertEquals(field_label, 'date posted')

    def test_last_edit_label(self):
        field_label = Comment._meta.get_field('last_edit').verbose_name
        self.assertEquals(field_label, 'last edit')

    def test_description_label(self):
        field_label = Comment._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        max_length = Comment._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    # custom class methods
    def test_comment_name_is_description(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = comment.description
        self.assertEquals(expected_object_name, str(comment))