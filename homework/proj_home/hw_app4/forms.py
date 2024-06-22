from django import forms
from .models import Client, Product, OrderItem, Order
from django.forms import inlineformset_factory


class ClientForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Иван"}),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@mail.ru"}
        ),
    )
    phone = forms.CharField(
        max_length=12,
        label="Телефон",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+1234567899 "}
        ),
    )
    address = forms.CharField(
        max_length=100,
        label="Адрес",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Москва, Ленина, д.120, кв.6"}
        ),
    )


class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Название товара",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Шоколад"}
        ),
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Горький"}
        ),
    )
    price = forms.DecimalField(
        label="Цена",
        max_digits=100,
        decimal_places=2,
        initial=0,
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "99"}
        ),
    )
    quantity = forms.IntegerField(
        label="Количество",
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    product_image = forms.ImageField(
        label="Изображение",
        widget=forms.FileInput(attrs={"class": "form-control", "type": "file"}),
    )


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]
        labels = {"product": "Товар", "quantity": "Количество товара"}
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["buyer"]
        labels = {"buyer": "Покупатель"}
        widgets = {"buyer": forms.Select(attrs={"class": "form-control"})}

    OrderItemFormSet = inlineformset_factory(
        Order, OrderItem, form=OrderItemForm, extra=3
    )
