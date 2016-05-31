from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from myblog.models import Post



class LatestEntriesFeed(Feed):

    title = "Bryan's Blog"
    link = "/"
    description = "Updates, changes and additions to Bryan's Blog."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

#   def item_link(self, item):
#       return reverse('blog_detail', kwargs={'post_id': self.pk})

