from django.shortcuts import render
from django.views import generic

from . models import Blogger, Blog

def index(request):
    """View function for home page of site."""
    num_blogs = Blog.objects.all().count()  
    num_bloggers = Blogger.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BloggerListView(generic.ListView):
    model = Blogger

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5