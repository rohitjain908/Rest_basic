from django.urls import path
from .views import article_detail, article_list

urlpatterns = [
  path('article_list',article_list,name="article_list"),
  path('article_list/<int:pk>',article_detail,name="article_detail")

]