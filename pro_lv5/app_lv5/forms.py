from django import forms
from django.contrib.auth.models import User
from app_lv5.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User    # gọi User mặc định của django
        fields = ('username', 'email', 'password')  # chỉ lấy các trường này thôi



class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo #gọi model  người dùng, do mình tự code thêm
        fields = ('portfolio_site', 'profile_pic')  #lấy các trường mà mình code thêm