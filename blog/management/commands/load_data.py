import json

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from blog.models import Post, Comment, Album, Photo, Todo
from users.models import Company, Address

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("data.json") as json_data:
            data = json.load(json_data)
            todos = data['todos']
            users = data['users']
            posts = data['posts']
            comments = data['comments']
            albums = data['albums']
            photos = data['photos']
            for user in users:
                name = user['name'].split()
                password = get_random_string(length=10)
                user_data = {**user, "first_name": name[0], "last_name": name[1], "password": password}
                user_data.pop('name')
                address_data = user_data.pop("address")
                company_data = user_data.pop("company")
                user = User.objects.create_user(**user_data)
                Address.objects.create(**address_data, user=user)
                Company.objects.create(**company_data, user=user)
            print("loaded users")
            for post in posts:
                Post.objects.get_or_create(**post)
            print("loaded posts")
            for comment in comments:
                Comment.objects.get_or_create(**comment)
            print("loaded comments")
            for album in albums:
                Album.objects.get_or_create(**album)
            print("loaded albums")
            for photo in photos:
                Photo.objects.get_or_create(**photo)
            print("loaded photos")
            for todo in todos:
                Todo.objects.get_or_create(**todo)
            print("loaded todos")
