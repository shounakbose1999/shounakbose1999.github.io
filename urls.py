"""quiztest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name ='index'),
    path('question0',views.correct,name='question0'),
    path('question1',views.quest1,name='question1'),
    path('rightanswer2',views.right,name='rightanswer2'),
    path('question2',views.ans2,name='question2'),
    path('question3',views.quest3,name='question3'),
    path('answer3',views.ans3,name='answer3'),
    path('question4',views.quest4,name='question4'),
    path('answer4',views.ans4,name='answer4'),
    path('allinone',views.all,name='allinone'),

]
