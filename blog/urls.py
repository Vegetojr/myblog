from django.urls import path
from .views import xd, tortuga, post_list, post_detail, post_share, post_comment  # PostListView
from .feeds import LatestPostsFeed
app_name = 'blog'

urlpatterns = [
    path("xd", xd, name="xd"),
    path("tortuga", tortuga, name="tortuga"),
    # path('', PostListView.as_view(), name='post_list'),
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path(
        '<int:post_id>/comment/', post_comment, name='post_comment'
    ),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
