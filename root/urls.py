"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from posts import views


urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')), 
    path('admin/', admin.site.urls),

    re_path(r'^(?:(?P<catid>\d+)/)?(?:(?P<q>\w+)/)?$', views.main_page, name="Main Page"),

    path('second', views.second, name="Second Page"),
    path('third', views.html_file, name="Third Page"),
    path('posts', views.getposts, name="Posts Page"),
    path('posts/save', views.savepost, name="Post Save Page"),
    path('post/<slug:myslug>/json', views.get_post_json, name="Post Get Json"),
    path('post/<slug:myslug>/<str:des>', views.getpost, name="Post Detail Page"),
    
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)