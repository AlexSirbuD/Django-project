from django.urls import path
from django.urls import re_path as url
from django.views.decorators.cache import cache_page

from .views import *



urlpatterns = [
    path('', StaffHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('contact/', StaffContact.as_view(), name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/edit/<slug:post_slug>/', UpdatePostView.as_view(), name='update_post'),
    path('post/<slug:post_slug>/delete/', DeletePostView.as_view(), name='delete_post'),
    # url(r'^pic_upload/(?P<user_id>\d+)/$', pic_upload, name='pic_upload'),
    path('my_posts/<str:username>/', MyPostsListView.as_view(), name='my_posts')

]

