from django.urls import path
from epicApp.views import HomeView, PostDetailView, AddPostView, UpdatePostView, \
    DeletePostView, AddCategoryView, category_view, category_list_view, like_view, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('remove/post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', category_view, name='category'),
    path('category/list/', category_list_view, name='category-list'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('comment/post/<int:pk>', AddCommentView.as_view(), name='add_comment')


]
