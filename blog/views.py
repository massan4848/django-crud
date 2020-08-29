from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Post
# Create your views here.
# class base view

class PostListView(ListView):
    model = Post  # 使うdatabase名
    template_name = 'blog/home.html'  
    # dataを渡して、表示させるファイル名,
    # blogアプリの中のtemplateファイル(自分で作る必要あり)の中のblogフォルダのhome.htmlを呼び出す。
    #　blogアプリとblogフォルダで別のものがあることに注意
    context_object_name = 'posts'  #databaseから取り出したデータをtemplateに渡す際の名前
    ordering = ['-date_posted']  # 並べる順番

class PostDetailView(DetailView):
    model = Post
    #default でtemplate_name = 'folder/post_<view名>.html'が割り当てられる。
    # default でcontext_object_name は'ojbect'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 