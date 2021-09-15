from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def article_list(request):

  if request.method=="GET":
    articles=Article.objects.all()
    serialize=ArticleSerializer(articles,many=True)
    return JsonResponse(serialize.data,safe=False)

  elif request.method=="POST":
    data=JSONParser().parse(request)
    serialize=ArticleSerializer(data=data)

    if serialize.is_valid():
      serialize.save()
      return JsonResponse(serialize.data,status=201)

    return JsonResponse(serialize.errors,status=400)

@csrf_exempt
def article_detail(request,pk):
  try:
    article=Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    return HttpResponse(status=404)

  if request.method=="GET":
    serialize=ArticleSerializer(article)
    return JsonResponse(serialize.data)

  elif request.method=="PUT":
    data=JSONParser().parse(request)
    serialize=ArticleSerializer(article,data=data)

    if serialize.is_valid():
      serialize.save()
      return JsonResponse(serialize.data)

    return JsonResponse(serialize.errors,status=400)

  elif request.method=="DELETE":
    article.delete()
    return HttpResponse(status=204)








