import requests

from django.core.management.base import BaseCommand

from forum.models import Address, Company, Post, User


USERS_URL = 'http://jsonplaceholder.typicode.com/users'
POSTS_URL = 'http://jsonplaceholder.typicode.com/posts'


class Command(BaseCommand):
    help = 'Парсинг данных'

    def handle(self, *args, **options):
        parse_users()
        parse_posts()


def get_data(url: str):
    response = requests.get(url)
    return response.json()


def parse_users():
    users_data = get_data(USERS_URL)

    for item in users_data:
        address_data = item['address']
        address, _ = Address.objects.get_or_create(
            city=address_data['city'],
            street=address_data['street'],
            suite=address_data['suite'],
            zipcode=address_data['zipcode'],
            lat=address_data['geo']['lat'],
            lng=address_data['geo']['lng']
        )

        company_data = item['company']
        company, _ = Company.objects.get_or_create(
            name=company_data['name'],
            catchphrase=company_data['catchPhrase'],
            bs=company_data['bs'],
        )

        User.objects.get_or_create(
            external_id=item['id'],
            name=item['name'],
            username=item['username'],
            email=item['email'],
            website=item['website'],
            phone=item['phone'],
            address=address,
            company=company
        )


def parse_posts():
    posts_data = get_data(POSTS_URL)

    for item in posts_data:
        user = User.objects.filter(external_id=item['userId']).first()
        if user:
            Post.objects.get_or_create(
                external_id=item['id'],
                title=item['title'],
                body=item['body'],
                user=user
            )
