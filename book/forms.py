from django import forms
from book.models import CommentBook


class PostCommentBook(forms.ModelForm):
	class Meta:
		model = CommentBook
		fields = ['body']


