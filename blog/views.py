from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from . models import Blogger, Blog, Comment

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

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogDetailView(generic.DetailView):
    model = Blog

class  CommentCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = Comment
    fields = ['description',]
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog object from the "pk" URL parameter and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment, return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})