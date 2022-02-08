

# Create your views here.
from datetime import datetime
from django.template import RequestContext
from django.shortcuts import render
from blogapp.models import BlogPost
from blogapp.forms import BlogPostForm
from django.http import HttpResponseRedirect
def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request,'blogapp/index.html', {'posts': posts})
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
            return HttpResponseRedirect('/blog/')
        else:
            form = BlogPostForm(request.POST)
            return render(request,'blogapp/create.html', {'form': form})
    else:
        form = BlogPostForm()
        return render(request,'blogapp/create.html', {'form': form})


