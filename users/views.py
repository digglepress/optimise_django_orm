from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()


# Create your views here.
def users_list(request):
    users = User.objects.all().values("first_name", "last_name", "id")
    context = {"users": users}
    return render(request, 'users/list.html', context=context)


def users_detail(request, pk):
    user = User.objects.prefetch_related("posts", "todos").get(pk=pk)
    context = {"user": user}
    return render(request, "users/detail.html", context=context)
