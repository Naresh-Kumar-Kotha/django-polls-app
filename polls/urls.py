from django.urls import path

from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),           # ex: /polls/
    path('home/', views.home, name='home'),         # ex: /polls/home/
    path('<int:question_id>/', views.detail, name='detail'),   # ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),   # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),       # ex: /polls/5/vote/
]

