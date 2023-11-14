from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path(r'songs/', views.SongList.as_view(), name='songs_list'),
    path(r'song/<str:lookup_param>/<value>', views.SongDetail.as_view(), name='song_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)