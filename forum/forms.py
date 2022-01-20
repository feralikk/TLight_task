from django import forms
from forum.models import User, Address, Company, Post


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
