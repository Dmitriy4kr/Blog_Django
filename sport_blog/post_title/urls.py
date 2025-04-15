from django.urls import path
from.views import AllPostsTitle, OnePostTitle

urlpatterns = [
    path('', AllPostsTitle.as_view(), name='all_posts'),
    path('<int:pk>/', OnePostTitle.as_view(), name='post')
]
