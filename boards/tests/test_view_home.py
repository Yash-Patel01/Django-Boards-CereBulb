from boards.models import Board, Post, Topic
from boards.views import home
from django.conf.urls import url
from django.test import TestCase
from django.urls import reverse, resolve

from ..views import board_topics, home, new_topic
from boards import views

class HomeTests(TestCase):
  
  def setUp(self) -> None:
    self.board = Board.objects.create(name="django",description="Django Board.")
    url = reverse('home')
    self.response = self.client.get(url)

  def test_home_view_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code,200)

  def test_home_url_resolves_home_view(self):
    view = resolve('/')
    self.assertEquals(view.func,home)

  def test_home_view_contains_link_to_topics_page(self):
    board_topics_url = reverse('board_topics',kwargs={'pk':self.board.pk})
    self.assertContains(self.response,'href="{0}"'.format(board_topics_url))
