"""
URL configuration for jatalian project.
"""

from django.contrib import admin
from django.urls import include, path

from words import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/login/', views.login_page, name='login'),

    path('', views.home, name='home'),
    path('vocabulary/', views.vocabulary, name='vocabulary'),
    path('new_word/', views.new_word, name='new_word'),

    path('delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
    path('learned_word/<int:word_id>/', views.learned_word, name='learned_word'),
    path('voice_word/<int:word_id>/', views.voice_word, name='voice_word'),
]
