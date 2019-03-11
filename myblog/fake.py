import random
from myblog.models import Admin, Post, Category, Comment, Link
from myblog.extensions import db
from faker import Faker
from sqlalchemy.exc import IntegrityError

fake = Faker()


def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='FakeBlog',
        blog_sub_title="I'm a fake blog",
        name='Whale Liu',
        about='um....I actually a fake blog.',

    )
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    categories = Category(name='Default')
    db.session.add(categories)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(1500),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)

        # from admin
        comment = Comment(
            author='Whale Liu',
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            from_admin=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    salt = int(count/10)
    # replies
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()


def fake_links():
    twitter = Link(name='Twitter', url='#')
    facebook = Link(name='Facebook', url='#')
    linkedin = Link(name='LinkedIn', url='#')
    google = Link(name='Google+', url='#')
    db.session.add_all([twitter, facebook, linkedin, google])
    db.session.commit()
