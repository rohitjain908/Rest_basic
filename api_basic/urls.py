from django.urls import path
from .views import GenericAPIView

urlpatterns = [
  path('generic/article_list/<int:id>',GenericAPIView.as_view()),
  path('generic/article_list',GenericAPIView.as_view())
]