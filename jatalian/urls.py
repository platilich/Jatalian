"""
URL configuration for jatalian project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import include, path

from words import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),

    path('delete_word/<int:word_id>', views.delete_word, name='delete_word'),
    path('learned_word/<int:word_id>', views.learned_word, name='learned_word'),
    path('voice_word/<int:word_id>', views.voice_word, name='voice_word'),

    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path('new_word/', views.new_word, name='new_word'),


]
