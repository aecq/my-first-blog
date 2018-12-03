from django.shortcuts import render
from django.views import generic

from .models import Blog
import markdown

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blog/blog_list.html'
	context_object_name = 'blogs'
	
	def get_queryset(self):
		return Blog.objects.all()
	
# class DetailView(generic.DetailView):
	# model = Blog
	# template_name = 'blog/detail.html'

def detail(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	blog_content = markdown.markdown(blog.content)
	context = {'blog': blog, 'blog_content': blog_content}
	return render(request, 'blog/detail.html', context)