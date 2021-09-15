from django.urls import path
from .views import ArticleAPIView,ArticleDetails

urlpatterns = [
  path('article_list',ArticleAPIView.as_view(),name="article_list"),
  path('article_list/<int:id>',ArticleDetails.as_view(),name="article_detail")
]