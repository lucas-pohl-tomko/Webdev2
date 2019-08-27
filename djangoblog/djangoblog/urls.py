"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from app.views import (
    PostCreate, PostUpdate, users, UserProfile, post, UserProfileEditAdmin,
    UserFollow, UserUnfollow, Index, index_all, index_followed,model_form_upload, homedoc, letra_list,letra_view,
    letra_create,letra_update,letra_delete, doc_delete

)

urlpatterns = [
    path('', letra_list, name='index'),
    path('homedoc/', homedoc, name='homedoc'),
    path('index-all', index_all, name='index-all'),
    path('index-follow', index_followed, name='index-followed'),
    path('post/add/', PostCreate.as_view(), name='author-add'),
    path('post/<int:id>/', post, name='post'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', users, name='users'),
    path('docpost/', model_form_upload, name='docpost'),
    path('user/<str:username>/', UserProfile.as_view(), name='user'),
    path(
        'user/<str:username>/edit', UserProfileEditAdmin.as_view(),
        name='edit_profile_admin'
    ),
    path(
        'user/<str:follower>/follows/<str:followed>/', UserFollow.as_view(),
        name='follow'
    ),
    path(
        'user/<str:follower>/unfollows/<str:followed>/',
        UserUnfollow.as_view(), name='unfollow'
    ),
    path(
        'user/<str:username>/followers/',
        UserProfile.as_view(), name='followers'
    ),
    path('letra', letra_list, name='letra_list'),
    path('view/<int:pk>', letra_view, name='letra_view'),
    path('new', letra_create, name='letra_new'),
    path('edit/<int:pk>', letra_update, name='letra_edit'),
    path('delete/<int:pk>', letra_delete, name='letra_delete'),
    path('deletedoc/<int:pk>', doc_delete, name='doc_delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)