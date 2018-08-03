from django.shortcuts import render


def index(request):
    """首页视图"""
    if request.method == 'GET':
        return render(request, 'index/index.html')


def publish_article(request):
    """发布文章"""
    if request.method == 'GET':
        return render(request, 'article/publish_article.html')

    if request.method == 'POST':
        pass




