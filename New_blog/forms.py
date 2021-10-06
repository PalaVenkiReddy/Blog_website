from django import forms
from .models import Post, Category

# to have all the categories from database
choices = Category.objects.all().values_list('name','name')
# choices are actually represented as follows 
#choices = [('sports', 'sports'), ('education', 'education'), ('coding', 'coding'),]


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('place', 'author', 'category', 'Description', 'post_image')

		widgets = {
		    # from bootstrap we can include form-control class to have a particular style 
		    'place': forms.TextInput(attrs={'class': 'form-control'}),
		    'author': forms.Select(attrs={'class': 'form-control'}),
		    'category': forms.Select(choices=choices, attrs={'class': 'form-control'}), # Note: use choices infront of attrs otherwise it doesn't work properly
		    'Description': forms.Textarea(attrs={'class': 'form-control'}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('place', 'category', 'Description','post_image')

		widgets = {
		    'place': forms.TextInput(attrs={'class': 'form-control'}),
		    'author': forms.Select(attrs={'class': 'form-control'}),
		    'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
		    'Description': forms.Textarea(attrs={'class': 'form-control'}),
		}


