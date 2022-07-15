from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost, Program


def home_screen_view(request):
    
    context = {}
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_update'), reverse=True)
    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)

def program_screen_view(request):
    
    context = {}
    program_posts = sorted(Program.objects.all(), key=attrgetter('date_update'), reverse=True)
    context['program_posts'] = program_posts

    return render(request, "personal/download.html", context)