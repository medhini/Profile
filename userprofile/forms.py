from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile 
        fields = ('Follow', 'About me : ', 'picture')
