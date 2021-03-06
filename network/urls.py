from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API paths
    path("posts/<str:post_parameter>", views.get_posts, name="posts"),
    path("post", views.create_or_update_post, name="update"),
    path("users/<str:username>", views.get_profile, name="profile"),
    path("likes/<int:post_id>", views.adjust_likes, name="like"),
    path("follow/<str:username>", views.adjust_follow, name="follow")
]
