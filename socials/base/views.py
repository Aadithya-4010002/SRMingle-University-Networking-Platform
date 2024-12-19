from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.views.generic import DetailView,CreateView
from django.contrib.auth.views import PasswordChangeView
from .models import *
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Profile
from .models import NewsPost

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile  # Assign the current user's profile as the author
            post.save()
            return redirect('home')  # Redirect to home or any other appropriate page
    else:
        form = PostForm()
    return render(request, 'base/add_post.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import AddNewsPostForm

def add_news_post(request):
    if request.method == 'POST':
        form = AddNewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            news_post = form.save()
            return redirect('newsfeed')  # Redirect to the 'newsfeed' URL name
    else:
        form = AddNewsPostForm()
    return render(request, 'base/addnewspost.html', {'form': form})




def academia_page(request):
    return render(request, 'base/academia.html')

def clubsinformations(request):
    return render(request, 'base/clubsinformations.html')

def postclickview(request):
    return render(request, 'base/postclickview.html')

def eventscalender(request):
    return render(request, 'base/eventscalender.html')

def placementscareer(request):
    return render(request, 'base/placementscareer.html')

def clubsforums(request):
    return render(request, 'base/clubsforums.html')


def accsettings(request):
    return render(request, 'base/accsettings.html')

def evencal(request):
    return render(request, 'base/evencal.html')

def oddcal(request):
    return render(request, 'base/oddcal.html')


def addnewspost(request):
    # Add your logic here for handling the add news post functionality
    # For example, if you want to render the addnewspost.html template:
    return render(request, 'base/addnewspost.html')

# views.py

from django.shortcuts import render
from .models import Post  # Import your Post model

def newsfeed(request):
    # Retrieve posts for the newsfeed (you may need to adjust this query based on your data model)
    newsfeed_posts = Post.objects.all()

    return render(request, 'base/newsfeed.html', {'newsfeed_posts': newsfeed_posts})


def srmngleintroduction(request):
    return render(request, 'base/srmngleintroduction.html')


# views.py

from django.shortcuts import render, redirect
from .forms import AddNewsPostForm
from django.shortcuts import render, redirect
from .forms import AddNewsPostForm

# views.py


# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import NewsPost
from .forms import AddNewsPostForm





# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Post
import random

@login_required(login_url='signup')
def home(request):
    try:
        user_object = request.user
        user_profile = Profile.objects.get(user=user_object)
    except Profile.DoesNotExist:
        # Redirect the user to create their profile if it doesn't exist
        return redirect('create_profile_page')

    all_users = User.objects.all()
    all_posts = Post.objects.all()
    all_profile = Profile.objects.all()
    count_posts = len(all_posts)

    my_user = [user_profile]
    suggestion_users = []

    for user in all_profile:
        if user not in my_user:
            suggestion_users.append(user)

    random.shuffle(suggestion_users)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'all_users': all_users,
        'all_posts': all_posts,
        'all_profile': all_profile,
        'count_posts': count_posts,
        'suggestion_users': suggestion_users,
    }
    return render(request, "base/home.html", context)



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/Otherprofile.html'

    def get_context_data(self,*args,**kwargs):
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        logged_in_user_posts = Post.objects.filter(author=page_user)

        if FollowersCount.objects.filter(user=page_user).first():
            button_text='UnFollow'
        else:
            button_text='Follow'

        user_followers=len(FollowersCount.objects.filter(user=page_user))
        user_following=len(FollowersCount.objects.filter(follower=page_user))

        num_posts=len(logged_in_user_posts)
        context["page_user"]=page_user
        context['logged_in_user_posts']=logged_in_user_posts
        context['num_posts']=num_posts
        context['button_text']=button_text
        context['user_followers']=user_followers
        context['user_following']=user_following
        return context
    
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        login_username=request.POST.get('username', None)
        user_password=request.POST["password"]
        user = authenticate(request,username=login_username, password = user_password)
        if user is not None:
            auth_login(request, user)
            messages.add_message(request, messages.INFO, 'You have successfully logged in.')
            return redirect('/')

        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
            return render(request,"base/login.html")

    return render(request,"base/login.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        email=email.rstrip()

        if email == '' or password == '' or username == '':
            messages.error(request,"Please fill all the fields.")
            return render(request,"base/signup.html")
        
        elif User.objects.filter(username=username).exists(): 
            messages.add_message(request, messages.INFO, 'Username already exists.')
            return render(request,"base/signup.html")
        
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email already exists.')
            return render(request,"base/signup.html")

        else :
            user = User.objects.create(email=email, username=username, password=make_password(password))
            user.save() 
            auth_login(request, user)    
            messages.add_message(request, messages.INFO, 'You have successfully signed up.')
            return redirect('/create_profile_page')
    else:
        return render(request,"base/signup.html")
    

def logout(request):
    auth_logout(request)
    return redirect('/')

class FriendView(ListView):
    model = Profile
    template_name = 'base/friends.html'
    profiles=Profile.objects.all()
    ordering = ['-id']

    def get_context_data(self,*args,**kwargs):
        context=super(FriendView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile)
        context["page_user"]=page_user
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'

class CreateProfilePageView(CreateView):
    model = Profile
    form_class=ProfilePageForm
    template_name="base/create_user_profile.html"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class=EditProfileNewForm
    template_name='base/edit_profile_page.html'
    success_url=reverse_lazy('home')


class PasswordsChangeView(PasswordChangeView):
       form_class= PasswordChangingForm
       success_url= reverse_lazy('password_success')

def password_success(request):
    return render(request, 'base/password_success.html', {})

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'base/add_comment.html'

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)


@login_required(login_url='signup')
def like_post(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    post=Post.objects.get(id=post_id)
    like_filter=LikePost.objects.filter(post_id=post_id,username=username).first()

    if like_filter==None:
        new_like=LikePost.objects.create(post_id=post_id,username=username)
        new_like.save()

        post.no_of_likes=post.no_of_likes+1
        post.save()
        return redirect('/')

    else:
        like_filter.delete()
        post.no_of_likes=post.no_of_likes-1
        post.save()
        return redirect('/')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'base/delete_post.html'
    success_url = reverse_lazy('home')

@login_required(login_url='signup')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = Profile.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'base/search.html', { 'user_profile':user_profile,'username_profile_list': username_profile_list,'username_profile':username_profile})

class UpdatePostView(UpdateView):
    model = Post
    form_class=EditForm
    template_name = 'base/update_post.html'

@login_required(login_url='signup')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/')
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/')
    else:
        return redirect('/')
    


# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete the user account
        request.user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')  # Redirect to home page or another appropriate view

    return render(request, 'base/delete_account_confirmation.html')

def postclickview(request):
    # Retrieve the data you want to display in postclickview.html
    # For example, let's say you want to display all posts
    all_posts = Post.objects.all()

    
    return render(request, 'base/postclickview.html', {'all_posts': all_posts})






