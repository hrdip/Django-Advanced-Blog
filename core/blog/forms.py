from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "status", "category", "published_date")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs['class'] = 'form-control'
        self.fields["content"].widget.attrs['class'] = 'form-control'
        self.fields["status"].widget.attrs['class'] = 'form-check-input mb-3'
        self.fields["category"].widget.attrs['class'] = 'form-control'
        self.fields["published_date"].widget.attrs['class'] = 'form-control'
        self.fields["published_date"].widget.attrs['type'] = 'datetime-local'
