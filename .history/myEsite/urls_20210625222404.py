from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
]
