from django.contrib import admin

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('title', )
    list_filter = ('title', 'is_published',)
    list_editable = ('is_published', )
    search_fields = ('title', 'id', )
    fields = ('title', 'category', 'content', 'photo',   'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('views', 'created_at', 'updated_at')
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
