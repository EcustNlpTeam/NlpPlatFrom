from django.db import models

# Create your models here.
class NLP(models.Model):
    name = models.CharField(max_length=20)

class UserInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    pass_word = models.CharField(max_length=64)
    user_token = models.CharField(max_length=64)
    token_last_modified = models.DateTimeField()
    task_state = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

class CrawlerTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_state = models.BooleanField(default=True)
    user_name = models.CharField(max_length=30)
    platform = models.CharField(max_length=30)
    account = models.CharField(max_length=30)
    weChatID = models.CharField(max_length=30)
    crawl_start = models.DateTimeField()
    crawl_end = models.DateTimeField()
    task_start = models.DateTimeField()
    task_end = models.DateTimeField()

    def __str__(self):
        return self.account

