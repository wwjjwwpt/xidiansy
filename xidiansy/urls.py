"""xidiansy URL Configuration

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
from django.urls import path

from django.contrib import admin
from django.urls import path
from django.urls import include,path
from fzsy.views import login
from fzsy.views import homepage, showpost, showpost1, showpost2 ,showpost4, showpost3,showyqj,showsyqc
from fzsy.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),
    path('post1/<slug:slug>/', showpost1),
    path('post2/<slug:slug>/', showpost2),
    path('post3/<slug:slug>/', showpost3),
    path('post4/<slug:slug>/', showpost4),
    path('yqj/<slug:slug>/', showyqj),
    path('syqc/<slug:slug>/', showsyqc),
    path('login/', login),
    path('logout/',logout)
]

