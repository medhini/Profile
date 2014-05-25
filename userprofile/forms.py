from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile 
        fields = ('Allow_email_notifications', 'About_me')
