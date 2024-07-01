from django.contrib import admin
from .models import Product, Order, Client, OrderItem
from .admin_mixins import ExportAsCSVMixin


@admin.action(description="Обнулить количество")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.action(description="Сменить имя на VIP")
def reset_name(modeladmin, request, queryset):
    queryset.update(name="VIP")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "register_date"]
    ordering = ["name"]
    list_filter = ["address", "phone"]
    search_fields = ["name", "address"]
    search_help_text = "Поиск по имени и адресу"
    readonly_fields = ["register_date"]
    actions = [reset_name]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],  # максимально широко в панели
                "fields": ["name"],
            },
        ),
        (
            "Контакты",
            {
                "classes": ["collapse"],  # изночально поле свернуто
                "fields": ["email", "phone", "address"],
            },
        ),
        (
            "Дата регистрации",
            {
                "fields": ["register_date"],
            },
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "quantity", "product_add_date"]
    ordering = ["title", "-quantity"]
    list_filter = ["price"]
    search_fields = ["title"]
    search_help_text = "Поиск по названию"
    readonly_fields = ["product_add_date"]
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["title", "description"],
            },
        ),
        (
            "Изображение товара",
            {
                "fields": ["product_image"],
            },
        ),
        (
            "Цена и количество",
            {
                "fields": ["price", "quantity"],
            },
        ),
        (
            "Дата поступления товара",
            {
                "fields": ["product_add_date"],
            },
        ),
    ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    inlines = [OrderItemInline]
    list_display = ["buyer", "total_amount", "order_date"]
    ordering = ["-order_date", "buyer"]
    list_filter = ["order_date"]
    search_fields = ["buyer"]
    search_help_text = "Поиск по Клиенту"
    readonly_fields = ["order_date"]
    actions = ['export_as_csv']
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["buyer"],
            },
        ),
        (
            "Сумма и дата заказа",
            {
                "fields": ["total_amount", "order_date"],
            },
        ),
    ]
