from django.urls import path, include

from blog import views

app_name = 'blog'
urlpatterns = [
    path('posts/', include([
            path('', views.post_list, name="post_list"),
            path('<int:pk>', views.post_detail, name="post_detail"),
        ]))
]
