import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace="blog")),
    path('users/', include('users.urls', namespace="users")),
]
