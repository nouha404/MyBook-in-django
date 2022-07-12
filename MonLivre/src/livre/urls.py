from django.urls import path
from livre.views import Index, PageTwo, Article,ArticleTwo,ArticleThree,ArticleFour,ArticleFive,ArticleSix,ArticleSeven,ArticleEight,ArticleNine

urlpatterns = [
    path('', Index, name="page-article"),
    path('matiere/', PageTwo, name="page-two"),
    path('article/', Article, name="article"),
    path('personnage/', ArticleTwo, name="personnage"),
    path('hacking/', ArticleThree, name="hacking"),
    path('nouvelle-aire/', ArticleFour, name="nouvelle-aire"),
    path('demarrage-du-hack/', ArticleFive, name="demarrage-du-hack"),
    path('des-gens-chez-moi/', ArticleSix, name="des-gens-chez-moi"),
    path('welcome-back/', ArticleSeven, name="welcome-back"),
    path('fail/', ArticleEight, name="fail"),
    path('professor/', ArticleNine, name="professor"),


]