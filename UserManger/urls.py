"""UserManger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView

#from authentication.views import login_page,logout_user,LoginPage
from blog.views import home,photo_upload,blog_and_photo_upload,view_blog,edit_blog,create_multiple_photos,follow_users
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',LoginView.as_view(template_name='authentication/login.html',
        redirect_authenticated_user=True),name='login'),

    path('logout/',LogoutView.as_view(),name='logout'),

    path('change-password',PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html',
    ),name='change_password'),

    path('change-password-done',PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ),name='change-password-done'),

    path('home/',home,name='home'),

    path('signup/',authentication.views.signup_page,name='signup'),

    path('photo/upload/',photo_upload,name='photo_upload'),

    
    path('blog/create', blog_and_photo_upload, name='blog_create'),

    path('blog/<int:blog_id>',view_blog, name='view_blog'),

    path('blog/<int:blog_id>/edit', edit_blog, name='edit_blog'),

     path('photo/upload-multiple/', create_multiple_photos,
    name='create_multiple_photos'),

    path('follow-users/', follow_users, name='follow_users')

]



from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)