from celery import shared_task


# Sends email for 500 users each 1 minute, so it won't take too loong
@shared_task
def send_email():
    from user.models import User
    from api.models import Post
    users = User.objects.filter().all()
    for user in users[:500]:
        last_posts = Post.objects.filter(
            blog__in=user.followed_blogs.all()
        ).order_by('-created_time')[:5]
        print(f'Sending email with last posts for {user.username}')
        print(last_posts.all())
