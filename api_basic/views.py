from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])##now web page is changed
def article_list(request):

  if request.method=="GET":
    articles=Article.objects.all()
    serialize=ArticleSerializer(articles,many=True)
    return Response(serialize.data)

  elif request.method=="POST":
    serialize=ArticleSerializer(data=request.data)##call create function of articleserlizer class
    # and create the instance of following data

    if serialize.is_valid():
      serialize.save()
      return Response(serialize.data,status=status.HTTP_201_CREATED)##status 201:-Created success status response

    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)##status 400:-Bad Request response status

@api_view(['GET','PUT','DELETE'])##now web page is changed
def article_detail(request,pk):
  try:
    article=Article.objects.get(pk=pk)##1 based indexing
  except Article.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)##status 404:-page not found

  if request.method=="GET":
    serialize=ArticleSerializer(article)
    return Response(serialize.data)

  elif request.method=="PUT":##update the data
    serialize=ArticleSerializer(article,data=request.data)##call update function of articleserlizer class and update this instance with following data

    if serialize.is_valid():
      serialize.save()
      return Response(serialize.data)

    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

  elif request.method=="DELETE":
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)








