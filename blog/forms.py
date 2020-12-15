from django import forms


class RegisterForm(forms.Form):
       user_name = forms.CharField(label='User Name', max_length=4000)
       email = forms.EmailField()
       password = forms.CharField(widget=forms.PasswordInput())


class CreatePostForm(forms.Form):
       title = forms.CharField(max_length=1000)
       short_body = forms.CharField(max_length=5000)
       blog_img = forms.ImageField()
       body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body'}))


class CreateCommentForm(forms.Form):
       body = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Comment"}), label='Comment ')