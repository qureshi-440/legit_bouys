from django import forms
from .models import UserProfile,Post,Comments

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("bio","profilepic","website_url","facebook_url","instagram_url","twitter_url","pintrest_url")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['bio'].label = "Bio"
        self.fields['profilepic'].label = "Profile Picture"
        self.fields["website_url"].label = "Website link (optional)"
        self.fields["facebook_url"].label = "Facebook (optional) "
        self.fields["instagram_url"].label = "Instagram (Optional) "
        self.fields["twitter_url"].label = "Twitter (Optional) "
        self.fields["pintrest_url"].label = "Pintrest (Optional)"

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","category","thumbnail","body")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["title"].label = "Blog Title"
        self.fields["category"].label = "Category"
        self.fields["thumbnail"].label = "Blog Thumbnail"
        self.fields["body"].label = "Content"

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("thumbnail","body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("message",)

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["message"].label = "Comment"

