from django.db import models
from django.contrib.auth.models import User
from better_profanity import profanity
from .news_classifier import classify_news  # Import the classifier function

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    classification = models.CharField(max_length=10, blank=True)  # 'Fake' or 'Real'
    confidence = models.FloatField(default=0.0)  # Percentage

    def save(self, *args, **kwargs):
        # Censor offensive words
        self.text = profanity.censor(self.text)

        # Classify the news text
        label, confidence = classify_news(self.text)
        self.classification = label
        self.confidence = confidence

        super().save(*args, **kwargs)

    @property
    def is_fake(self):
        return self.classification == "Fake" and len(self.text.split()) > 10

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=200, choices=[('upvote', 'Upvote'), ('downvote', 'Downvote')])

    def __str__(self):
        return f'{self.user.username} - {self.vote_type}'