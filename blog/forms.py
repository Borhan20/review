from .models import Comment,Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body':forms.Textarea(attrs={'rows':5})
        }

        

        
        