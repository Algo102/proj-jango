from django.contrib import admin
from .models import Author, Article, FlipCoin, Comment
from .admin_mixins import ExportAsCSVMixin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ('title', 'text', 'pub_date', 'author', 'category', 'views', 'is_published')
    readonly_fields = ['pub_date']
    actions = ['export_as_csv']

# Вместо
# admin.site.register(Article, ArticleAdmin)
# написали
# @admin.register(Article)


@admin.action(description='Сменить имя на None')
def get_none(modeladmin, request, queryset):
    queryset.update(name='None')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'bio', 'birthday']
    ordering = ['-name', 'birthday']
    list_filter = ['email', 'birthday']
    search_fields = ['bio']
    search_help_text = 'Поиск по биографии'
    actions = [get_none]

    # fields = ['name', 'last_name', 'email', 'bio', 'birthday']
    readonly_fields = ['birthday']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],  # максимально широко в панели
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],  # изначально поле свернуто
                'description': 'Фамилия и биография',
                'fields': ['last_name', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
        (
            'Хронология',
            {
                'description': 'Дата рождения',
                'fields': ['birthday'],
            }
        ),
    ]


# admin.site.register(Author)
# admin.site.register(Article)
admin.site.register(FlipCoin)
admin.site.register(Comment)

# Другой вариант написания
# myModels = [Author, Article, FlipCoin, Comment]
# admin.site.register(myModels)

# Еще вариант
# admin.site.register([Article, FlipCoin, Comment, Author])

admin.site.register(Author, AuthorAdmin)
