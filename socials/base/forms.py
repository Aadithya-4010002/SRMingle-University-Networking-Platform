from .models import Profile,Post,Comment
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from django import forms
from .models import Profile




class EditProfileNewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'fname', 'lname', 'description', 'profileimg')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
            'profileimg': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

        labels = {
            'username': 'Username',  # Change labels as per your requirements
            'fname': 'First Name',
            'lname': 'Last Name',
            'description': 'Description',
            'profileimg': 'Profile Image',
        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
       model=Profile
       fields = ('username','fname','lname','description','profileimg')

       widgets={
          'username':forms.TextInput(attrs={'class':'form-control'}),
          'fname':forms.TextInput(attrs={'class':'form-control'}),
          'lname':forms.TextInput(attrs={'class':'form-control'}),
          'description':forms.Textarea(attrs={'class':'form-control'}), 
        }
    labels = {
            'username': 'Username',  # Change labels as per your requirements
            'fname': 'First Name',
            'lname': 'Last Name',
            'description': 'Description',
            'profileimg': 'Profile Image',
        }

from django import forms
from .models import Post
from django.contrib.auth.models import User

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'caption', 'location', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'style': 'margin-top: 10px; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content', 'style': 'margin-top: 10px; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location', 'style': 'margin-top: 10px; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'margin-top: 10px; width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;'}),
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super(PostForm, self).__init__(*args, **kwargs)

        # Limit choices for the author field to the current authenticated user
        if user:
            self.fields['author'] = forms.ModelChoiceField(queryset=User.objects.filter(username=user.username))

        # Provide choices for the location field
        # For example, a list of countries/cities
        # You can replace these choices with your own list
        self.fields['location'] = forms.ChoiceField(choices=[
    ('University Building', 'University Building'), 
    ('Java', 'Java'), 
    ('UB Food Joint', 'UB Food Joint'),
    ('BEL Lab', 'BEL Lab'),

    ('Canteen Building', 'Canteen Building'),
    ('PG Block', 'PG Block'),
    ('Hi Tech Block', 'Hi Tech Block'),
    ('Mechanical block', 'Mechanical block'),
    ('Workshop', 'Workshop'),
    ('Heat Engineering Lab', 'Heat Engineering Lab'),
    ('Computer science block', 'Computer science block'),
    ('Electrical science block', 'Electrical science block'),
    ('Hydraulics lab Annexure', 'Hydraulics lab Annexure'),
    ('Main Block', 'Main Block'),
    ('Library building', 'Library building'),
    ('Office Building', 'Office Building'),
    ('Office Annexure', 'Office Annexure'),
    ('Student Activity (Performing Arts)', 'Student Activity (Performing Arts)'),
    ('Post office building', 'Post office building'),
    ('University', 'University'),
    ('International Hostel', 'International Hostel'),
    ('Meenakshi Womens Hostel', 'Meenakshi Womens Hostel'),
    ('Staff Quarters', 'Staff Quarters'),
    ('Principal Residence', 'Principal Residence'),
    ('Guest House', 'Guest House'),
    ('Sannasi hostel IV', 'Sannasi hostel IV'),
    ('Sannasi hostel V', 'Sannasi hostel V'),
    ('Sannasi hostel VI', 'Sannasi hostel VI'),
    ('Sannasi hostel VII', 'Sannasi hostel VII'),
    ('Sannasi hostel VIII', 'Sannasi hostel VIII'),
    ('Staff Quarters Block A & B', 'Staff Quarters Block A & B'),
    ('M.B.A.Hostel', 'M.B.A.Hostel'),
    ('M.B.A.Block', 'M.B.A.Block'),
    ('M.B.A.Annexure I', 'M.B.A.Annexure I'),
    ('M.B.A.Annexure II', 'M.B.A.Annexure II'),
    ('Bio Tech block', 'Bio Tech block'),
    ('IT Park', 'IT Park'),
    ('Auditorium', 'Auditorium'),
    ('International Hostel -II', 'International Hostel -II'),
    ('New Kitchen \'F\' Block', 'New Kitchen \'F\' Block'),
    ('Men\'s Hostel IV Kitchen Block II', 'Men\'s Hostel IV Kitchen Block II'),
    ('Aeronautical', 'Aeronautical'),
    ('MBA Canteen Extension - III', 'MBA Canteen Extension - III'),
    ('Science & Humanities', 'Science & Humanities'),
], widget=forms.Select(attrs={'class': 'form-control'}))



class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type':'password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model= User
        fields = ('old_password','new_password1','new_password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
       }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','title_tag','author','caption','location','image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'username'}),
            'caption':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
        }

# forms.py
from django import forms
from .models import NewsPost

class AddNewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ('title', 'body', 'datetime', 'contact', 'attachment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Announcement Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Announcement Body'}),
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Information'}),
        }

