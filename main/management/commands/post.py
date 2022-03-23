from django.core.management import BaseCommand
from main.models import Post, Category
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = []
        faker = False
        for i in range(1000):
            fake = Faker()
            posts.append(
                Post(
                    category=Category.objects.order_by("?").first(),
                    subject=fake.name() if faker else f"Subject {i}",
                    content=fake.text() if faker else f"Content {i}"
                )
            )
        Post.objects.bulk_create(posts)
