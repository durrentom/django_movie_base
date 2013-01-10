from django.forms import ModelForm
from comments.models import *
from django.forms.widgets import HiddenInput

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		widgets={
			'movie' : HiddenInput()
		}