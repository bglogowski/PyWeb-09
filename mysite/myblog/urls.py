from django.conf.urls import url

from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view
from myblog.views import add_post

from myblog.feeds import LatestEntriesFeed

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
    url(r'^latest/feed/$',
         LatestEntriesFeed(),
         name='rss_feed'),
    url(r'^add/post$', 
        add_post, 
        name='blog_add_post'),
]
