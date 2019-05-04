"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import serve
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    # 上传图片预览
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # markdown
    path('mdeditor/', include('mdeditor.urls'))
]

handler500 = 'blog.views.page_500'
# handler404 = 'blog.views.page_404'
