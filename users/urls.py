from django.urls import path, include

from users import views

app_name = 'users'
urlpatterns = [
    path("", include([
            path("", views.users_list, name="list"),
            path("<int:pk>", views.users_detail, name="detail")
        ]))
]
