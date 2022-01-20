from django.contrib import admin

from .forms import UserForm, PostForm, AddressForm, CompanyForm
from .models import User, Address, Company, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email', 'phone', 'website')
    form = UserForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'user')
    form = PostForm


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'catchphrase', 'bs')
    form = CompanyForm


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'suite', 'city', 'zipcode', 'lat', 'lng')
    form = AddressForm
