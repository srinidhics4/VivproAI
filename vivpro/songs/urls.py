from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path(r'songs/', views.SongList.as_view()),
    path(r'song/<title>', views.SongDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)