from django.contrib import admin

from blog.models import BlogPost, Program

# admin.site.register(BlogPost)
@admin.register(BlogPost)
class Admin(admin.ModelAdmin):
    fields = ('title', 'body', 'image', 'author', 'slug', )
    list_display = ('title', 'date_published', 'date_update', )
    list_filter = ('title',)

@admin.register(Program)
class Admin1(admin.ModelAdmin):
    fields = ('title', 'body', 'image', 'document', 'author', )
    list_display = ('title', 'date_published', 'date_update',)
    list_filter = ('title',)
