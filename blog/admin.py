from django.contrib import admin
from blog.models import Post, BlogComment,Category

admin.site.register((BlogComment))
@admin.register(Post)
@admin.register(Category)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)