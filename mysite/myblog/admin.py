from django.contrib import admin
from django.core.urlresolvers import reverse
from myblog.models import Category, Post
import datetime

def make_published(modeladmin, request, queryset):
    now = datetime.datetime.now()
    queryset.update(published_date=now)

make_published.short_description = "Set date and time for selected posts"


class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)
    actions = (make_published,)

    list_display = (
        '__unicode__',
        'author_for_admin',
        'created_date',
        'modified_date',
        'published_date',
    )

    fields = (
        'title',
        'text',
        'author',
        'published_date',
        ('created_date', 'modified_date'),
    )

    readonly_fields = (
        'created_date',
        'modified_date',
    )

    def author_for_admin(self, obj):
        author = obj.author
        url = reverse('admin:auth_user_change', args=(author.pk,))
        name = author.get_full_name() or author.username
        link = '<a href="{}">{}</a>'.format(url, name)
        return link

    author_for_admin.short_description = 'Author'
    author_for_admin.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
