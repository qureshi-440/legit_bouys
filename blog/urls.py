from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog' 

urlpatterns = [
    path("",views.PostList.as_view(),name='home'),
    path("create-profile/",views.profile.as_view(),name="profile_create"),
    path("profile_page/<username>/",views.profile_page,name="profile_page"),
    path("profile-update/<username>/<pk>/",views.update_profile.as_view(),name='profile_update'),
    path("create-post/",views.postcreate.as_view(),name='create_post'),
    path("post-detail/<slug>/",views.postdetail.as_view(),name='post_detail'),
    path("like-post/<pk>/",views.likeview,name="post_like"),
    path("post-update/<slug>/<pk>/",views.postUpdate.as_view(),name='post_update'),
    path("post-delete/<slug>/<pk>/",views.postDelete.as_view(),name="post_delete"),
    path("post-detail/<slug>/comment/",views.CommentCreate.as_view(),name="create_comment"),
    path("delete-comment/<slug>/<pk>/",views.CommentDelete.as_view(),name="comment_delete"),
    path("follow/<pk>",views.follow_user,name="follow")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL ,document_root= settings.MEDIA_ROOT)