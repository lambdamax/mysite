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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urls = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = urls + [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    re_path(r'static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # 上传图片预览
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # markdown
    path('mdeditor/', include('mdeditor.urls')),
    path('wb', views.wb, name='wb'),
    path('api/spider', views.SinaSpider.as_view(), name='sinaspider'),
]

# handler500 = 'blog.views.page_500'
# handler404 = 'blog.views.page_404'
