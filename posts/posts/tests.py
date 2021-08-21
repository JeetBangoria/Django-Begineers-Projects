#At the top we imported the TestCase module which lets us create a sample database and our Post model.
from django.urls import reverse
from django.test import TestCase
from .models import Post

#At the top we imported the TestCase module which lets us create a sample database and our Post model.
class PostModelTest(TestCase):

    #This is to create a post.
    def setUp(self):
        Post.objects.create(text='just a text')

    # To check our created post ... Remember to give name as test_ in starting
    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}' #The next line uses f strings, a very cool addition to Python 3.6, which let us put variables directly in our strings as long as the variables are surrounded by brackets {}. 
        self.assertEqual(expected_object_name,'just a text') #we use assertEqual to check that our newly created entry does in fact match what we input at the top.

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')