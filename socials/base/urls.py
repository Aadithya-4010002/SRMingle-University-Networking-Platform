from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPostView,EditProfilePageView,CreateProfilePageView,PasswordsChangeView,FriendView,AddCommentView,DeletePostView,UpdatePostView,ShowProfilePageView
from .views import delete_account
from .views import academia_page
from .views import newsfeed
from .views import addnewspost
from .views import srmngleintroduction
from .views import eventscalender
from .views import placementscareer
from .views import clubsforums
from .views import accsettings
from .views import evencal
from .views import oddcal
from .views import clubsinformations
from .views import postclickview
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup,name='signup'),
    path('newsfeed/', newsfeed, name='newsfeed'),
    path('addnewspost/', addnewspost, name='addnewspost'),
    path('eventscalender/', eventscalender, name='eventscalender'),
    path('placementscareer/', placementscareer, name='placementscareer'),
    path('clubsforums/', clubsforums, name='clubsforums'),
    path('evencal/', evencal, name='evencal'),
    path('oddcal/', oddcal, name='oddcal'),
    path('academia/', academia_page, name='academia_page'),
    path('postclickview/', postclickview, name='postclickview'),
    path('clubsinformations/', clubsinformations, name='clubsinformations'),
    path('accsettings/', accsettings, name='accsettings'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_news_post/', AddPostView.as_view(), name='add_news_post'),
    path('srmngleintroduction/', srmngleintroduction, name='srmngleintroduction'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name='show_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('password/',PasswordsChangeView.as_view(template_name='base/change-password.html')),
    path('password_success/', views.password_success, name="password_success"),
    path('friends/',FriendView.as_view(),name='friends'),
    path('post/<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
    path('like-post',views.like_post,name='like-post'),
    path('post/<int:pk>/remove',DeletePostView.as_view(),name="delete_post"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('delete_account/', delete_account, name='delete_account'),
    path('search',views.search,name='search'),
    path('follow',views.follow,name='follow')
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)