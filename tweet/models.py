from django.db import models
from django.contrib.auth.models import User
from better_profanity import profanity

# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=1000)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    upvotes = models.PositiveIntegerField(default=0)  # New field
    downvotes = models.PositiveIntegerField(default=0)  # New field

    def save(self, *args, **kwargs):
        # Censor offensive words in the tweet text
        self.text = profanity.censor(self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=200, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')])

    def __str__(self):
        return f'{self.user.username} - {self.vote_type}'