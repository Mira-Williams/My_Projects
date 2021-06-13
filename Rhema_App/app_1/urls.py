from django.urls import path
from . import views, initialize

urlpatterns = [
    path('', views.main),
    path('initialize', initialize.initialize),
    path('choose_book', views.choose_book),
    path('choose_chapter', views.choose_chapter),
    path('choose_verse', views.choose_verse),
    path('verse_link', views.verse_link),
    path('clear_session', views.clear_session),
    path('filter_error', views.filter_error),
]

