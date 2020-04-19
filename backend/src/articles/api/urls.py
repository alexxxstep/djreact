from django.urls import path, include
from .view import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
]

