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
from django.urls import path
from django.contrib.auth.models import Group
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import employment_policy,leave_policy,other_policy

admin.site.site_header='Welcome to NSL'
admin.site.index_title = "Contact Manager"
from .settings import DEBUG,MEDIA_URL,MEDIA_ROOT
admin.site.unregister(Group)
urlpatterns = [
    #path('admin/',current_datetime),
    path('admin/', admin.site.urls),
    path('admin/employment_policy.html/',employment_policy),
    path('admin/leave_policy.html/',leave_policy),
    path('admin/other_policy.html/',other_policy),

]
# urlpattern= [
#     url(r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home/'}),
# ]


if DEBUG:
    urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)