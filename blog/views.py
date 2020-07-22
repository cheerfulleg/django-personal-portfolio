from django.shortcuts import render, get_object_or_404

from .models import Blog


def blog_list(request):
    context = {
        'blogs': Blog.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/blog.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
