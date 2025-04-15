from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages
from .models import PostTitle
from post_content.models import PostContent


class AllPostsTitle(ListView):
    model = PostTitle
    template_name = 'post_title/all_posts.html'
    context_object_name = 'posts'


class OnePostTitle(DetailView):
    model = PostTitle
    template_name = 'post_title/one_post.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        try:
            self.object.postcontent
        except PostContent.DoesNotExist:
            messages.warning(request, "У этой статьи пока нет контента.")
            return redirect('all_posts')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = self.object.postcontent
        return context
