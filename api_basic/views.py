from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ArticleAPIView(APIView):

  def get(self,request):
    articles=Article.objects.all()
    serialize=ArticleSerializer(articles,many=True)
    return Response(serialize.data)

  def post(self,request):
    serialize=ArticleSerializer(data=request.data)

    if serialize.is_valid():
      serialize.save()
      return Response(serialize.data,status=status.HTTP_201_CREATED)
    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

  def get_object(self,id):
    try:
      return Article.objects.get(id=id)
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def get(self,request,id):
    try:
      article=Article.objects.get(id=id)
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serialize=ArticleSerializer(article)
    return Response(serialize.data)

  def put(self,request,id):
    try:
      article=Article.objects.get(id=id)
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    serialize=ArticleSerializer(article,data=request.data)
    if serialize.is_valid():
      serialize.save()
      return Response(serialize.data)

    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,id):
    try:
      article=Article.objects.get(id=id)
    except Article.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

