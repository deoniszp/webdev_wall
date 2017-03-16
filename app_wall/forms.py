from django import forms
from .models import Message, Comment

# form from message
class MessageForm(forms.ModelForm):
    text = forms.CharField(min_length=1, required=True, widget=forms.Textarea(attrs={
        'class': 'custom-control',
        'placeholder': 'Input your message...',
        'rows': 4,
    }), label="")

    class Meta:
        model = Message
        fields = ['text']

class CommentForm(forms.ModelForm):
    text = forms.CharField(min_length=1, required=True, widget=forms.Textarea(attrs={
        'class': 'custom-control',
        'placeholder': 'Input your comment...',
        'rows': 3,
    }), label="")

    message_id = forms.CharField(widget=forms.HiddenInput,required=True, label="")
    parent_id = forms.CharField(widget=forms.HiddenInput,required=False, label="", initial=None)

    class Meta:
        model = Comment
        exclude = ('user', 'message', 'parent',)