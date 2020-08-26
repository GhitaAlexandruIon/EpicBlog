from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from epicApp.forms import PostForm, CommentForm
from epicApp.models import Post, Category, Comment


from django.contrib.auth import get_user_model
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Prefetch

User = get_user_model()


class HomeView(ListView):
    model = Post
    cats = Category.objects.all()
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 7

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UserPost(generic.ListView):
    model = Post
    template_name = '../epicApp/templates/user_post_list.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.post_user = User.objects.all().perfetch_related(Prefetch('post')).get(
            username__iexact=self.kwargs.get('username'))

    def get_queryset(self):
        try:
            self.post_user = User.objects.all().perfetch_related(Prefetch('post')).get(
                username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(**kwargs)
        votes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = votes.total_likes()
        liked = False
        if votes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(DetailView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def category_view(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})


def category_list_view(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
