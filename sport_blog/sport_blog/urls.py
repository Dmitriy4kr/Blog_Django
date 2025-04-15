from django.contrib import admin
from django.urls import path, include
from sport_blog import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('post_title.urls')),
    path('', main_views.index),
]
