from django.shortcuts import render
from livre.models import BooksModel


# Create your views here.


def Index(request):
    books = BooksModel.objects.all()
    return render(request, 'page_one.html', {'books': books})


def PageTwo(request):
    books = BooksModel.objects.all()
    return render(request, 'page_two.html', {'books': books})


def Article(request):
    books = BooksModel.objects.get(id='1')
    return render(request, 'article.html', {'books': books})


def ArticleTwo(request):
    books = BooksModel.objects.get(id='2')
    return render(request, 'article_two.html', {'books': books})


def ArticleThree(request):
    books = BooksModel.objects.get(id='3')
    return render(request, 'article_tree.html', {'books': books})


def ArticleFour(request):
    books = BooksModel.objects.get(id='4')
    return render(request, 'article_four.html', {'books': books})


def ArticleFive(request):
    books = BooksModel.objects.get(id='5')
    return render(request, 'article_five.html', {'books': books})


def ArticleSix(request):
    books = BooksModel.objects.get(id='6')
    return render(request, 'article_six.html', {'books': books})


def ArticleSeven(request):
    books = BooksModel.objects.get(id='7')
    return render(request, 'article_seven.html', {'books': books})


def ArticleEight(request):
    books = BooksModel.objects.get(id='8')
    return render(request, 'article_eight.html', {'books': books})


def ArticleNine(request):
    books = BooksModel.objects.get(id='9')
    return render(request, 'article_nine.html', {'books': books})

