from django.shortcuts import render
from .models import Post
from django.shortcuts import render_to_response
from products.models import Product
from users.models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	posts = Post.objects.all()
	context = {
		'posts' : posts
	}
	return render(request, "home.html", context)

# class based views
class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'blog/post_form.html'
	fields = ['content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'blog/post_form.html'
	fields = ['content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'blog/post_confirm_delete.html'
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


# class based view for home end


def about(request):
	dummy = 'coding'
	context = {
		'dummy' : dummy
	}
	return render(request, "about.html", context)

def contact(request):
	dummy = 'coding'
	context = {
		'dummy' : dummy
	}
	return render(request, "contact.html", context)